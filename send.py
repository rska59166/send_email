import pandas as pandas as pd
import yagmail
from time timport sleep

contacts_df = pd.read_csv('여기에 csv파일 경로를 입력해주세요')

yag=yagmail.SMTP('이메일 주소를 입력해주세요', '비밀번호를 입력해주세요')

for index, contact in contacts_df.iterrows():
    print(f"이메일 보내는 중: {contact['이메일']}")
    yag.send(
        to=contact['이메일'],
        subject='안녕하세요! 이메일 보내기 테스트 중입니다.',
        contents=f"안녕하세요, {contact['이름']}! 이메일 보내기 테스트 중입니다. 감사합니다."
    )
    print(f"이메일 보내기 성공: {contact['이메일']}")
    sleep(1)
