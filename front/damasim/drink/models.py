from django.db import models

# Create your models here.

class Bev14Prep(models.Model):
    myunknowncolumn = models.IntegerField(db_column='MyUnknownColumn', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    coca_cola_classic_coke = models.IntegerField(db_column='Coca-Cola Classic Coke', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coca_cola_zero_sugar = models.IntegerField(db_column='Coca-Cola Zero Sugar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pepsi = models.IntegerField(db_column='Pepsi', blank=True, null=True)  # Field name made lowercase.
    pepsi_zero_sugar_lime = models.IntegerField(db_column='Pepsi Zero Sugar Lime', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sprite = models.IntegerField(db_column='Sprite', blank=True, null=True)  # Field name made lowercase.
    mountain_dew = models.IntegerField(db_column='Mountain Dew', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fanta_orange = models.IntegerField(db_column='Fanta Orange', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chilsung_cider = models.IntegerField(db_column='Chilsung Cider', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    welchs_grape_soda = models.IntegerField(db_column='Welchs Grape Soda', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    milkis = models.IntegerField(db_column='Milkis', blank=True, null=True)  # Field name made lowercase.
    mccol = models.IntegerField(db_column='McCol', blank=True, null=True)  # Field name made lowercase.
    sunkist_sparkling_grapefruit_soda = models.IntegerField(db_column='Sunkist sparkling grapefruit soda', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    demisoda_apple_soda_drink = models.IntegerField(db_column='Demisoda Apple Soda Drink', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oran_c_calamansi = models.IntegerField(db_column='Oran C Calamansi', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ambasa = models.IntegerField(db_column='AMBASA', blank=True, null=True)  # Field name made lowercase.
    schweppes_lemon_soda = models.IntegerField(db_column='Schweppes Lemon Soda', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sunny_10_pineapple = models.IntegerField(db_column='Sunny 10 Pineapple', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    naranged_cider = models.IntegerField(db_column='Naranged Cider', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_7up = models.IntegerField(db_column='7up', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    tejava = models.IntegerField(db_column='Tejava', blank=True, null=True)  # Field name made lowercase.
    pine_bud_drink = models.IntegerField(db_column='Pine bud Drink', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_2_field = models.IntegerField(db_column='2%', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    gatorade = models.IntegerField(db_column='Gatorade', blank=True, null=True)  # Field name made lowercase.
    pocari_sweat = models.IntegerField(db_column='Pocari Sweat', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    powerade = models.IntegerField(db_column='Powerade', blank=True, null=True)  # Field name made lowercase.
    toreta = models.IntegerField(db_column='Toreta', blank=True, null=True)  # Field name made lowercase.
    hot6ix = models.IntegerField(db_column='HOT6ix', blank=True, null=True)  # Field name made lowercase.
    bacchus = models.IntegerField(db_column='Bacchus', blank=True, null=True)  # Field name made lowercase.
    number_500vita_500 = models.IntegerField(db_column='500Vita 500', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    monster_energy = models.IntegerField(db_column='Monster energy', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    monster_energy_ultra = models.IntegerField(db_column='Monster energy Ultra', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coronamin_c = models.IntegerField(db_column='COronamin C', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guangdong_corn_silk_tea = models.IntegerField(db_column='Guangdong Corn Silk Tea', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guangdong_raisin_tea = models.IntegerField(db_column='Guangdong Raisin Tea', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    woongjin_sky_barley = models.IntegerField(db_column='Woongjin Sky Barley', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hitejinro_black_barley = models.IntegerField(db_column='HiteJinro Black Barley', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_17namyang_dairy_17tea = models.IntegerField(db_column='17Namyang Dairy 17Tea', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    guangdong_jujube_ssanghwa = models.IntegerField(db_column='Guangdong Jujube Ssanghwa', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lipton_iced_tea = models.IntegerField(db_column='Lipton Iced Tea', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    burdock_tea_for_a_day = models.IntegerField(db_column='Burdock tea for a day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    guangdong_jinssanghwa = models.IntegerField(db_column='Guangdong Jinssanghwa', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sweet_vegemil_b = models.IntegerField(db_column='Sweet Vegemil B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vegemil_black_bean_high_calcium = models.IntegerField(db_column='Vegemil Black Bean High Calcium', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vegemil_black_beans_and_black_sesame_seeds = models.IntegerField(db_column='Vegemil black beans and black sesame seeds', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gtnamyang_delicious_soymilk_gt = models.IntegerField(db_column='GTNamyang delicious soymilk GT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vegemil_almonds_and_walnuts = models.IntegerField(db_column='Vegemil Almonds and Walnuts', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cantata_coffee = models.IntegerField(db_column='Cantata Coffee', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_maxim_t_o_p = models.IntegerField(db_column='..Maxim T.O.P', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    barista_rules = models.IntegerField(db_column='Barista Rules', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    georgia = models.IntegerField(db_column='Georgia', blank=True, null=True)  # Field name made lowercase.
    lets_be = models.IntegerField(db_column='Lets Be', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    french_cafe_roastery = models.IntegerField(db_column='French Cafe Roastery', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    my_cafe_latte = models.IntegerField(db_column='My Cafe Latte', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    a_cafe_la_size_up = models.IntegerField(db_column='A cafe la size up', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_100_seoul_milk = models.IntegerField(db_column='100%Seoul Milk', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    gtdelicious_milk_gt = models.IntegerField(db_column='GTdelicious milk GT', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    banana_milk = models.IntegerField(db_column='Banana Milk', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chocolate_doraemon = models.IntegerField(db_column='Chocolate Doraemon', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delmont_mango = models.IntegerField(db_column='Delmont Mango', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    minute_maid_orange = models.IntegerField(db_column='Minute Maid Orange', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sunkist_lemonade = models.IntegerField(db_column='Sunkist Lemonade', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nature_is_aloe = models.IntegerField(db_column='Nature is aloe', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_100_juice_in_the_morning_100_orange = models.IntegerField(db_column='100% Juice in the morning 100% Orange', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    haitai_hulled_pear = models.IntegerField(db_column='Haitai hulled pear', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delmont_cold_orange = models.IntegerField(db_column='Delmont Cold Orange', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gaya_farm_tomatoes = models.IntegerField(db_column='Gaya Farm Tomatoes', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sunup_fruit_vegetable_salad = models.IntegerField(db_column='Sunup Fruit Vegetable Salad', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lotte_jeju_love_tangerine_love = models.IntegerField(db_column='Lotte Jeju Love Tangerine Love', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    minute_maid_aloe = models.IntegerField(db_column='Minute Maid Aloe', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'bev14_prep'

    def __str__(self):
        return self.myunknowncolumn