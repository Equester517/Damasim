from django.db import models

# Create your models here.

class Bev14Prep(models.Model):
    myunknowncolumn = models.IntegerField(db_column='MyUnknownColumn', blank=True, null=True)  # Field name made lowercase.
    코카콜라_coca_cola_classic_coke_field = models.IntegerField(db_column='코카콜라(Coca-Cola Classic Coke)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    코카콜라_제로_coca_cola_zero_sugar_field = models.IntegerField(db_column='코카콜라 제로(Coca-Cola Zero Sugar)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    펩시콜라_pepsi_field = models.IntegerField(db_column='펩시콜라(Pepsi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    펩시_제로슈거_라임_pepsi_zero_sugar_lime_field = models.IntegerField(db_column='펩시 제로슈거 라임(Pepsi Zero Sugar Lime)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    스프라이트_sprite_field = models.IntegerField(db_column='스프라이트(Sprite)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    마운틴_듀_mountain_dew_field = models.IntegerField(db_column='마운틴 듀(Mountain Dew)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    환타_fanta_orange_field = models.IntegerField(db_column='환타(Fanta Orange)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    칠성_사이다_chilsung_cider_field = models.IntegerField(db_column='칠성 사이다(Chilsung Cider)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    웰치스_포도_welchs_grape_soda_field = models.IntegerField(db_column='웰치스 포도(Welchs Grape Soda)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    밀키스_milkis_field = models.IntegerField(db_column='밀키스(Milkis)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    맥콜_mccol_field = models.IntegerField(db_column='맥콜(McCol)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    썬키스트_소다_자몽_sunkist_sparkling_grapefruit_soda_field = models.IntegerField(db_column='썬키스트 소다 자몽(Sunkist sparkling grapefruit soda)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    데미소다_demisoda_apple_soda_drink_field = models.IntegerField(db_column='데미소다(Demisoda Apple Soda Drink)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    오란씨_깔라만시_oran_c_calamansi_field = models.IntegerField(db_column='오란씨 깔라만시(Oran C Calamansi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    암바사_ambasa_field = models.IntegerField(db_column='암바사(AMBASA)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    슈웹스_레몬토닉_schweppes_lemon_soda_field = models.IntegerField(db_column='슈웹스 레몬토닉(Schweppes Lemon Soda)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    써니텐_파인애플_sunny_10_pineapple_field = models.IntegerField(db_column='써니텐 파인애플(Sunny 10 Pineapple)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    나랑드_사이다_naranged_cider_field = models.IntegerField(db_column='나랑드 사이다(Naranged Cider)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    세븐업_7up_field = models.IntegerField(db_column='세븐업(7up)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    데자와_tejava_field = models.IntegerField(db_column='데자와(Tejava)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    솔의_눈_pine_bud_drink_field = models.IntegerField(db_column='솔의 눈(Pine bud Drink)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    이프로_2_field = models.IntegerField(db_column='이프로(2%)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    게토레이_gatorade_field = models.IntegerField(db_column='게토레이(Gatorade)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    포카리스웨트_pocari_sweat_field = models.IntegerField(db_column='포카리스웨트(Pocari Sweat)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    파워에이드_powerade_field = models.IntegerField(db_column='파워에이드(Powerade)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    토레타_toreta_field = models.IntegerField(db_column='토레타(Toreta)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    핫식스_hot6ix_field = models.IntegerField(db_column='핫식스(HOT6ix)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    박카스_bacchus_field = models.IntegerField(db_column='박카스(Bacchus)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    비타500_vita_500_field = models.IntegerField(db_column='비타500(Vita 500)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    몬스터에너지_monster_energy_field = models.IntegerField(db_column='몬스터에너지(Monster energy)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    몬스터에너지_울트라_monster_energy_ultra_field = models.IntegerField(db_column='몬스터에너지 울트라(Monster energy Ultra)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    오로나민c_oronamin_c_field = models.IntegerField(db_column='오로나민C(Oronamin C)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    광동_옥수수_수염차_guangdong_corn_silk_tea_field = models.IntegerField(db_column='광동 옥수수 수염차(Guangdong Corn Silk Tea)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    광동_헛개차_guangdong_raisin_tea_field = models.IntegerField(db_column='광동 헛개차(Guangdong Raisin Tea)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    웅진_하늘보리_woongjin_sky_barley_field = models.IntegerField(db_column='웅진 하늘보리(Woongjin Sky Barley)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    하이트진로_블랙보리_hitejinro_black_barley_field = models.IntegerField(db_column='하이트진로 블랙보리(HiteJinro Black Barley)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    남양유업_17차_namyang_dairy_17tea_field = models.IntegerField(db_column='남양유업 17차(Namyang Dairy 17Tea)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    광동_대추쌍화_guangdong_jujube_ssanghwa_field = models.IntegerField(db_column='광동 대추쌍화(Guangdong Jujube Ssanghwa)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    립톤_아이스티_복숭아_lipton_iced_tea_field = models.IntegerField(db_column='립톤 아이스티 복숭아(Lipton Iced Tea)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    잘빠진_하루_우엉차_burdock_tea_for_a_day_field = models.IntegerField(db_column='잘빠진 하루 우엉차(Burdock tea for a day)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    광동_진쌍화_guangdong_jinssanghwa_field = models.IntegerField(db_column='광동 진쌍화(Guangdong Jinssanghwa)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    달콤한_베지밀_비_sweet_vegemil_b_field = models.IntegerField(db_column='달콤한 베지밀 비(Sweet Vegemil B)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    베지밀_검은콩_고칼슘_vegemil_black_bean_high_calcium_field = models.IntegerField(db_column='베지밀 검은콩 고칼슘(Vegemil Black Bean High Calcium)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    베지밀_검은콩과_검은참깨_vegemil_black_beans_and_black_sesame_seeds_field = models.IntegerField(db_column='베지밀 검은콩과 검은참깨(Vegemil black beans and black sesame seeds)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    남양_맛있는_두유_gt_namyang_delicious_soymilk_gt_field = models.IntegerField(db_column='남양 맛있는 두유 GT(Namyang delicious soymilk GT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    베지밀_아몬드와_호두_vegemil_almonds_and_walnuts_field = models.IntegerField(db_column='베지밀 아몬드와 호두(Vegemil Almonds and Walnuts)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    칸타타_커피_cantata_coffee_field = models.IntegerField(db_column='칸타타 커피(Cantata Coffee)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    맥심_티_오_피_maxim_t_o_p_field = models.IntegerField(db_column='맥심 티.오.피(Maxim T.O.P)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    바리스타룰스_barista_rules_field = models.IntegerField(db_column='바리스타룰스(Barista Rules)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    조지아_georgia_field = models.IntegerField(db_column='조지아(Georgia)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    레쓰비_lets_be_field = models.IntegerField(db_column='레쓰비(Lets Be)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    프렌치카페_로스터리_french_cafe_roastery_field = models.IntegerField(db_column='프렌치카페 로스터리(French Cafe Roastery)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    마이_카페라떼_my_cafe_latte_field = models.IntegerField(db_column='마이 카페라떼(My Cafe Latte)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    아카페라_사이즈업_a_cafe_la_size_up_field = models.IntegerField(db_column='아카페라 사이즈업(A cafe la size up)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    서울우유_나_100_seoul_milk_field = models.IntegerField(db_column='서울우유 나 100%(Seoul Milk)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    맛있는_우유_gt_delicious_milk_gt_field = models.IntegerField(db_column='맛있는 우유 GT(delicious milk GT)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    바나나맛_우유_banana_milk_field = models.IntegerField(db_column='바나나맛 우유(Banana Milk)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    초코에몽_chocolate_doraemon_field = models.IntegerField(db_column='초코에몽(Chocolate Doraemon)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    델몬트_망고_delmont_mango_field = models.IntegerField(db_column='델몬트 망고(Delmont Mango)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    미닛메이드_오렌지주스_minute_maid_orange_field = models.IntegerField(db_column='미닛메이드 오렌지주스(Minute Maid Orange)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    썬키스트_레몬에이드_sunkist_lemonade_field = models.IntegerField(db_column='썬키스트 레몬에이드(Sunkist Lemonade)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    자연은_알로에_nature_is_aloe_field = models.IntegerField(db_column='자연은 알로에(Nature is aloe)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    아침에주스_100_오렌지_juice_in_the_morning_100_orange_field = models.IntegerField(db_column='아침에주스 100% 오렌지(Juice in the morning 100% Orange)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    해태_갈아만든_배_haitai_hulled_pear_field = models.IntegerField(db_column='해태 갈아만든 배(Haitai hulled pear)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    델몬트_콜드_오렌지_delmont_cold_orange_field = models.IntegerField(db_column='델몬트 콜드 오렌지(Delmont Cold Orange)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    가야농장_토마토_gaya_farm_tomatoes_field = models.IntegerField(db_column='가야농장 토마토(Gaya Farm Tomatoes)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    썬업_과일야채샐러드_sunup_fruit_vegetable_salad_field = models.IntegerField(db_column='썬업 과일야채샐러드(Sunup Fruit Vegetable Salad)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    롯데_제주사랑_감귤사랑_lotte_jeju_love_tangerine_love_field = models.IntegerField(db_column='롯데 제주사랑 감귤사랑(Lotte Jeju Love Tangerine Love)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    미닛메이드_알로에_minute_maid_aloe_field = models.IntegerField(db_column='미닛메이드 알로에(Minute Maid Aloe)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'bev14_prep'
