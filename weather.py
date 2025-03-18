from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.params import ArgPlainText
from httpx import AsyncClient
from nonebot.matcher import Matcher
from nonebot.adapters.qq import MessageSegment
import inspect
import re

weather = on_command("天气", rule=to_me(), aliases={"weather", "查天气"}, priority=10, block=True)


@weather.handle()
async def handle_function(matcher: Matcher, args: Message = CommandArg()):
    # 提取参数纯文本作为地名，并判断是否有效
    if args.extract_plain_text():
        matcher.set_arg("location", args)


@weather.got("location", prompt="请输入地名（格式：省,市,区，例如：四川,成都,成华区）")
async def got_location(location: str = ArgPlainText()):
    # 拆分用户输入的地名
    # 初始化变量，避免在异常处理时出现问题
    province, city, county = None, None, None

    parts = re.split(r'[,，\s/]+', location)
    if len(parts) == 3:
        province, city, county = parts
    else:
        await weather.reject("输入格式不正确，请按省,市,区的格式输入！")
        return


    # 使用拆分后的省、市、区来构造 API 请求
    url = f"https://wis.qq.com/weather/common?source=pc&weather_type=observe|index|alarm|limit|tips&province={province}&city={city}&county={county}"

    # 获取天气数据
    async with AsyncClient() as session:
        resp = await session.post(url)
        r = resp.json()
        weather_message = f"今天的天气信息：\n"
        weather_message += f"天气状况：{r['data']['observe']['weather']}\n"
        weather_message += f"当前温度：{r['data']['observe']['degree']}°C\n"
        weather_message += f"湿度：{r['data']['observe']['humidity']}%\n"
        weather_message += f"风速：{r['data']['observe']['wind_direction_name']} {r['data']['observe']['wind_power']}级\n"

        # 针对生活场景的建议["data"]["index"]

        for index in r["data"]["index"].values():
            # 忽略 "time" 字段
            if isinstance(index, dict) and index['name'] == '穿衣':
                name = f"**{index['name']}**"
                info = index['info']
                detail = index['detail']
                weather_message += f"{name}：{info} - {detail}\n"

        # 附加的旅行建议
        weather_message += "\n【旅行提示】\n"
        weather_message += f"旅游：{r['data']['index']['tourism']['info']} - {r['data']['index']['tourism']['detail']}\n"

        # 添加交通建议
        weather_message += f"交通：{r['data']['index']['traffic']['info']} - {r['data']['index']['traffic']['detail']}\n"

        # 如果需要提供紫外线强度相关建议
        weather_message += f"紫外线强度：{r['data']['index']['ultraviolet']['info']} - {r['data']['index']['ultraviolet']['detail']}\n"

        # 最后更新的时间
        weather_message += f"\n最后更新：{r['data']['observe']['update_time']}"

        await weather.finish(f"{weather_message}")
