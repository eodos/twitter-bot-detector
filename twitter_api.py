#/usr/bin/env python3

from twitter import *
from api_keys import *

twitter = Twitter(
		auth = OAuth(access_key, access_secret, consumer_key, consumer_secret))

bot_accounts = "LaurenacostaFIT,Lizminniecats,appleiphone3gsx,JennaRay22,blairrogers,cliffwatson,Opallommie,WeighLossDrinks,Ginamzz,MarcyMillsap2,_Inspirational2,FitnessM0tiv,getzoncode,healthfitnesss9,TravelsGenius,follow_me_900,1healthtreasure,ainaali12,AmazingDeals20,GymFreeAbs,CindyLo26178854,JudithDinardo,BeFltWorld,iariarodrigue11,Agnes66632,VenusGifts,NBANewsBot,NailbiterBot,thewordoftheday,PowerVocabTweet,thejokeoftheday,Favstar_Bot,AbelDuarteBot,todoesbienBot,BklynMuseumBot,freezeframebot,Mythology,Both_champagne_bot,GenerateACat,everyailment,boy2bot,GIFsofWikipedia,MagicRealismBot,dscovr_epic,censusAmericans,FFD8FFDB,Botgle,TRAVIS_CJ_BOT,ReciteNews,SwachhBharatBot,StreamerBot"
nonbot_accounts = "Konyrodri,costadelrock,GretaKasatkina,PEstradaF92,PeperCalibu_73,Alejandro_1792,lunnith,Alexandralxn,jjepgfenix,Eusebio_770,DaniCTena,Josegd1992,JoseGarcaiDaiz,DestroPro,alvaro6malaga,Said_Oty,Popeitor,AVicDiaz,danirocri,OliverSostmannR,NataliaTaliita,jjepgfenix1,voirshn,Daniel_VGomez,javivb, bencweiner,LaurifromRHOC,SoulSwaggerChef,ShawnRabideau,tomcolicchio,topchefkevin,ashfulk,Teresa_Giudice,jayrayner1,chris_manzo,MadisonMalibu,ChefJenCarroll,JLJeffLewis,MarcusCooks,PadmaLakshmi,MVoltaggio,ChefBettyFraser,ChefRichSweeney,KELLYCHOI,daniellestaub,Andy,ChefRobinL,NeNeLeakes,chefludo,Jennipulos"

bot_results = twitter.users.lookup(screen_name=bot_accounts)
nonbot_results = twitter.users.lookup(screen_name=nonbot_accounts)

with open('accounts.csv', 'w', encoding='utf-8') as f:
	for user in bot_results:
		row = [user["id"], user["id_str"], user["screen_name"], user["location"], user["description"], user["url"], user["followers_count"], user["friends_count"], user["listed_count"], user["created_at"], user["favourites_count"], user["verified"], user["statuses_count"], user["lang"], user["status"], user["default_profile"], user["default_profile_image"], user["has_extended_profile"], user["name"], '1']
		str_row = ','.join(str(e) for e in row)
		f.write(str_row + '\n')

	for user in nonbot_results:
		row = [user["id"], user["id_str"], user["screen_name"], user["location"], user["description"], user["url"], user["followers_count"], user["friends_count"], user["listed_count"], user["created_at"], user["favourites_count"], user["verified"], user["statuses_count"], user["lang"], user["status"], user["default_profile"], user["default_profile_image"], user["has_extended_profile"], user["name"], '0']
		str_row = ','.join(str(e) for e in row)
		f.write(str_row + '\n')