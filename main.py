import flet as ft
import grass

def main(page: ft.Page):
    # 假设 data 是您从上文中获取的考试成绩数据
    #exams = [{'高2021级周考（2）理科': {'id': 16063, 'excelUrl': 'https://static.wtjy.com/temp/export/16063/kxyT0omI/115a2b58c68844614eb6ad5cc34e102a.zip', 'totalscore': 546.5, 'totalclassrank': 4, 'totalschoolrank': 334, 'scores': [{'subject': '语文', 'score': 102.0, 'classrank': 27, 'schoolrank': 687, 'answerpaperA': 'https://static.wtjy.com/temp/scan/86725/12/PC11762_86725_0012_0003_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/86725/12/PC11762_86725_0012_0003_B_adjust.jpg'}, {'subject': '数学', 'score': 93.0, 'classrank': 37, 'schoolrank': 1011, 'answerpaperA': 'https://static.wtjy.com/temp/scan/86726/8/PC11762_86726_0008_0003_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/86726/8/PC11762_86726_0008_0003_B_adjust.jpg'}, {'subject': '英语', 'score': 129.5, 'classrank': 2, 'schoolrank': 76, 'answerpaperA': 'https://static.wtjy.com/temp/scan/86727/5/PC11762_86727_0005_0003_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/86727/5/PC11762_86727_0005_0003_B_adjust.jpg'}, {'subject': '物理', 'score': 87.0, 'classrank': 4, 'schoolrank': 194, 'answerpaperA': 'https://static.wtjy.com/temp/scan/86728/2/PC11862_86728_0002_0002_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/86728/2/PC11862_86728_0002_0002_B_adjust.jpg'}, {'subject': '化学', 'score': 74.0, 'classrank': 19, 'schoolrank': 581, 'answerpaperA': 'https://static.wtjy.com/temp/scan/86728/2/PC11862_86728_0002_0002_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/86728/2/PC11862_86728_0002_0002_B_adjust.jpg'}, {'subject': '生物', 'score': 61.0, 'classrank': 21, 'schoolrank': 581, 'answerpaperA': 'https://static.wtjy.com/temp/scan/86728/2/PC11862_86728_0002_0002_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/86728/2/PC11862_86728_0002_0002_B_adjust.jpg'}, {'subject': '理综合', 'score': 222.0, 'classrank': 4, 'schoolrank': 320, 'answerpaperA': 'https://static.wtjy.com/temp/scan/86728/2/PC11862_86728_0002_0002_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/86728/2/PC11862_86728_0002_0002_B_adjust.jpg'}, {'subject': '日语', 'score': 0.0, 'classrank': 0, 'schoolrank': 0, 'answerpaperA': '', 'answerpaperB': ''}]}}, {'高2021级周考（1）理科': {'id': 15691, 'excelUrl': 'https://static.wtjy.com/temp/export/15691/8fAiBGmx/956b25ec9c2f0ead5ccd5c5a531fb803.zip', 'totalscore': 504.5, 'totalclassrank': 11, 'totalschoolrank': 519, 'scores': [{'subject': '语文', 'score': 95.0, 'classrank': 31, 'schoolrank': 795, 'answerpaperA': 'https://static.wtjy.com/temp/scan/85867/2/PC11805_85867_0002_0038_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/85867/2/PC11805_85867_0002_0038_B_adjust.jpg'}, {'subject': '数学', 'score': 94.0, 'classrank': 23, 'schoolrank': 883, 'answerpaperA': 'https://static.wtjy.com/temp/scan/85868/4/PC11862_85868_0004_0059_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/85868/4/PC11862_85868_0004_0059_B_adjust.jpg'}, {'subject': '英语', 'score': 130.5, 'classrank': 3, 'schoolrank': 186, 'answerpaperA': 'https://static.wtjy.com/temp/scan/85869/5/PC11862_85869_0005_0007_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/85869/5/PC11862_85869_0005_0007_B_adjust.jpg'}, {'subject': '物理', 'score': 53.0, 'classrank': 19, 'schoolrank': 696, 'answerpaperA': 'https://static.wtjy.com/temp/scan/85870/4/PC11805_85870_0004_0007_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/85870/4/PC11805_85870_0004_0007_B_adjust.jpg'}, {'subject': '化学', 'score': 60.0, 'classrank': 37, 'schoolrank': 716, 'answerpaperA': 'https://static.wtjy.com/temp/scan/85870/4/PC11805_85870_0004_0007_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/85870/4/PC11805_85870_0004_0007_B_adjust.jpg'}, {'subject': '生物', 'score': 72.0, 'classrank': 12, 'schoolrank': 337, 'answerpaperA': 'https://static.wtjy.com/temp/scan/85870/4/PC11805_85870_0004_0007_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/85870/4/PC11805_85870_0004_0007_B_adjust.jpg'}, {'subject': '理综合', 'score': 185.0, 'classrank': 18, 'schoolrank': 578, 'answerpaperA': 'https://static.wtjy.com/temp/scan/85870/4/PC11805_85870_0004_0007_A_adjust.jpg', 'answerpaperB': 'https://static.wtjy.com/temp/scan/85870/4/PC11805_85870_0004_0007_B_adjust.jpg'}, {'subject': '日语', 'score': 0.0, 'classrank': 0, 'schoolrank': 0, 'answerpaperA': '', 'answerpaperB': ''}]}}]

    global exams
    
    # 创建一个可滚动的视图，以适应可能的多个考试卡片
    page.scroll = True
    audio1 = ft.Audio(
        src="/ScoreTrackin'Superstar2.mp3", autoplay=True
        #src="/勇敢说不.mp3", autoplay=True
    )
    page.overlay.append(audio1)

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("大狗屎查成绩"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.MUSIC_OFF, on_click=lambda _: audio1.pause()),
        ],
    )
    page.add(ft.Text("数据加载需要时间，请耐心等待！", color=ft.colors.RED,))
    page.update()
    
    username = "lihao740"
    password = "1592580357"
    studentId = "3124644"

    access_token = grass.get_access_token(username, password)['access_token']
    examsinfo = grass.fetch_exams_info(access_token)
    exams = grass.exam_details(examsinfo, access_token, studentId)

    
    # 遍历数据以创建每个考试的卡片
    for exam_data in exams:
        for exam_name, details in exam_data.items():
            score_cards = [
                ft.Row(
                    [
                        ft.Text(f"{subject['subject']}:", size=16),
                        ft.Text(f"得分: {subject['score']}"),
                        ft.Text(f"班级排名: {subject['classrank']}"),
                        ft.Text(f"年级排名: {subject['schoolrank']}"),
                    ],
                    alignment="spaceAround"
                )
                for subject in details["scores"]
            ]

            subject_buttons = []

            # 为特定科目 “语文”, “数学”, “英语”, “理综” 创建答题卡按钮
            for subject in details["scores"]:
                if subject["subject"] in ["语文", "数学", "英语", "理综合"]:
                    answer_sheet_A = subject.get("answerpaperA")
                    answer_sheet_B = subject.get("answerpaperB")
                    subject_button = ft.ElevatedButton(
                        text=subject["subject"],
                        on_click=lambda _, a=answer_sheet_A, b=answer_sheet_B: (
                            page.launch_url(a), page.launch_url(b)
                        ) if a and b else None  # 只有当两个链接都存在时才会打开
                    )
                    subject_buttons.append(subject_button)

            # 创建查看Excel按钮
            excel_button = ft.ElevatedButton(
                text="查看Excel",
                on_click=lambda _, url=details["excelUrl"]: page.launch_url(url),
            )
            
            # 创建一个卡片来显示考试名称、成绩、排名和答题卡按钮
            exam_card = ft.Card(
                content=ft.Column(
                    [
                        ft.Text(exam_name, size=20, weight="bold"),
                        ft.Text(f"总分: {details['totalscore']}"),
                        ft.Text(f"班级排名: {details['totalclassrank']}"),
                        ft.Text(f"年级排名: {details['totalschoolrank']}"),
                        *score_cards,
                        ft.Row(subject_buttons, wrap=True),
                        excel_button
                    ],
                ),
            )

            page.add(exam_card)
            page.update()

    # 全部内容添加后一次性更新页面
    page.update()

ft.app(target=main)