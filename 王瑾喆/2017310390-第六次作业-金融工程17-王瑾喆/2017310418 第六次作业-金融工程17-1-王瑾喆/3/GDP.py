import json
import pygal
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """定义获取两个字母的国别码的函数"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

filename = 'gdp_json.json'

with open(filename) as f:
    gdp_data = json.load(f)
    
#
gdps={}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] ==2010:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            gdps[code] = gdp


#把gdp按照大小分为三组，存到三个字典中
gdps_1, gdps_2, gdps_3 = {}, {}, {}
for code, gdp in gdps.items():
    if gdp > 10000000000:
            gdps_1[code] = gdp
    elif gdp > 3000000000:
            gdps_2[code] = gdp
    else:
            gdps_3[code] = gdp
       
#输出分组后的图片
wm = pygal.maps.world.World()
wm.title = 'World GDP in 2010, by Country'
wm.add('group1', gdps_3)
wm.add('group2', gdps_2)
wm.add('group3', gdps_1)
wm.render_to_file('world_gdp.svg')
