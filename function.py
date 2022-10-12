import os
import requests
from all_dics import *
import time
from copy import deepcopy


def drop_scroll(browser):
    '''将滑条从头滚动到底,以便让浏览器充分加载'''
    for x in range(1, 11, 2):
        # time.sleep(0.5)
        j = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        browser.execute_script(js)

def create_folder(path):
    if os.path.exists(path):
        return 0
    os.mkdir(path)

def get_version(browser):
    version = browser.find_element_by_xpath('//button[@class = "css-ee3hyw e5qh6tw2"]/span').text.replace("Version: ","")
    create_folder(version)
    return version

def download_img(path,src):
    # 设置重连次数
    requests.session().adapters.DEFAULT_RETRIES = 5  # 设置默认重新尝试次数
    requests.session().close()
    pic = requests.get(src)  # 获得图片的网址
    fp = open(path, 'wb')  # 打开图片所在的路径
    fp.write(pic.content)  # 下载图片到本地
    fp.close()
    pic.close()  # 关闭get请求
    del (pic)  # 删除释放内存

def get_all_heros_pic(browser):
    drop_scroll(browser)  # 将滑条滑动到最下面
    pics = browser.find_elements_by_xpath("//aside//li//a")
    create_folder('hero_name')
    for pic in pics:
        try:
            src = pic.find_element_by_xpath("img").get_attribute("src")
        except Exception:
            src = pic.find_element_by_xpath("div/img").get_attribute("src")  # 比如像主星龙王这样的黑色带锁头像
        name = pic.find_element_by_xpath("span").text
        download_img(f'hero_name/' + hero_dict[name] + '.png', src)
        print(name)

def get_all_top_brief_info(browser):
    '''
    获得所有上路英雄的基本信息
    :param browser:
    :return:
    '''
    version = get_version(browser)
    drop_scroll(browser)  # 将滑条滑动到最下面
    heros = browser.find_elements_by_xpath("//table//tr") # 获得英雄表格中的所有行
    length = len(heros)
    result = ''
    for i in range(1,length,1):
        hero = heros[i]
        hero_attributes = hero.find_elements_by_xpath("td")
        name = hero_attributes[1].find_element_by_xpath("a/strong").text + '\t' # 姓名
        print(name)
        layer = hero_attributes[2].text+'\t' # 层级
        rate_of_victory = hero_attributes[3].text+'\t' # 胜率
        rate_of_pick = hero_attributes[4].text+'\t' # 选率
        rate_of_ban = hero_attributes[5].text+'+\t' # 禁用率
        three_weak_against = hero_attributes[6].find_elements_by_xpath("a/div/img")  # 这个地方前端经常维护，可能常做更改
        against_list = list()
        for against in three_weak_against:
            against_list.append(against.get_attribute('alt'))
        # against1 = three_weak_against[0].get_attribute('alt')+'\t'
        # against2 = three_weak_against[1].get_attribute('alt')+'\t'
        # against3 = three_weak_against[2].get_attribute('alt')+'\t'
        hero_result = name + layer + rate_of_victory + rate_of_pick + rate_of_ban + str(against_list) + '\n'
        result += hero_result
        print(hero_result)
    info = open(f'{version}/top.txt', mode='w') # 将结果写入文件
    info.write(result)
    info.close()


def get_all_jug_brief_info(browser):
    '''
    获得所有打野英雄的基本信息
    :param browser:
    :return:
    '''
    version = get_version(browser)
    # button = browser.find_element_by_xpath("//button[text()='打野']") # 找到打野的按钮
    # browser.execute_script("arguments[0].click();", button)
    browser.get('https://www.op.gg/champions?region=kr&tier=platinum_plus&position=jungle')
    time.sleep(0.5)
    drop_scroll(browser)
    time.sleep(0.5)
    heros = browser.find_elements_by_xpath("//table//tr") # 获得英雄表格中的每一行
    length = len(heros)
    result = ''
    for i in range(1,length,1):
        hero = heros[i]
        hero_attributes = hero.find_elements_by_xpath("td")
        name = hero_attributes[1].find_element_by_xpath("a/strong").text + '\t'
        layer = hero_attributes[2].text+'\t'
        rate_of_victory = hero_attributes[3].text+'\t'
        rate_of_pick = hero_attributes[4].text+'\t'
        rate_of_ban = hero_attributes[5].text+'+\t'
        three_weak_against = hero_attributes[6].find_elements_by_xpath("a/div/img") # 这个地方前端经常维护，可能常做更改
        against_list = list()
        for against in three_weak_against:
            against_list.append(against.get_attribute('alt'))
        # against1 = three_weak_against[0].get_attribute('alt')+'\t'
        # against2 = three_weak_against[1].get_attribute('alt')+'\t'
        # against3 = three_weak_against[2].get_attribute('alt')+'\t'
        hero_result = name + layer + rate_of_victory + rate_of_pick + rate_of_ban + str(against_list) + '\n'
        result += hero_result
        print(hero_result)
    info = open(f'{version}/jungle.txt', mode='w') # 将结果写入文件
    info.write(result)
    info.close()


def get_all_mid_brief_info(browser):
    '''
    获得所有中单英雄的基本信息
    :param browser:
    :return:
    '''
    version = get_version(browser)
    # button = browser.find_element_by_xpath("//button[text()='中单']") # 找到中单的按钮
    # browser.execute_script("arguments[0].click();", button)
    browser.get('https://www.op.gg/champions?region=kr&tier=platinum_plus&position=mid')
    time.sleep(1)
    drop_scroll(browser)
    time.sleep(1)
    heros = browser.find_elements_by_xpath("//table//tr") # 获得英雄表格中的每一行
    length = len(heros)
    result = ''
    for i in range(1,length,1):
        hero = heros[i]
        hero_attributes = hero.find_elements_by_xpath("td")
        name = hero_attributes[1].find_element_by_xpath("a/strong").text + '\t'
        layer = hero_attributes[2].text+'\t'
        rate_of_victory = hero_attributes[3].text+'\t'
        rate_of_pick = hero_attributes[4].text+'\t'
        rate_of_ban = hero_attributes[5].text+'+\t'
        three_weak_against = hero_attributes[6].find_elements_by_xpath("a/div/img")  # 这个地方前端经常维护，可能常做更改
        against_list = list()
        for against in three_weak_against:
            against_list.append(against.get_attribute('alt'))
        # against1 = three_weak_against[0].get_attribute('alt')+'\t'
        # against2 = three_weak_against[1].get_attribute('alt')+'\t'
        # against3 = three_weak_against[2].get_attribute('alt')+'\t'
        hero_result = name + layer + rate_of_victory + rate_of_pick + rate_of_ban + str(against_list) + '\n'
        result += hero_result
        print(hero_result)
    info = open(f'{version}/mid.txt', mode='w')  # 将结果写入文件
    info.write(result)
    info.close()


def get_all_ad_brief_info(browser):
    '''
    获得所有下路射手的基本信息
    :param browser:
    :return:
    '''
    version = get_version(browser)
    # button = browser.find_element_by_xpath("//button[text()='下路']") # 找到下路的按钮
    # browser.execute_script("arguments[0].click();", button)
    browser.get('https://www.op.gg/champions?region=kr&tier=platinum_plus&position=adc')
    time.sleep(0.5)
    drop_scroll(browser)
    time.sleep(0.5)
    heros = browser.find_elements_by_xpath("//table//tr") # 获得英雄表格中的每一行
    length = len(heros)
    result = ''
    for i in range(1,length,1):
        hero = heros[i]
        hero_attributes = hero.find_elements_by_xpath("td")
        name = hero_attributes[1].find_element_by_xpath("a/strong").text + '\t'
        layer = hero_attributes[2].text+'\t'
        rate_of_victory = hero_attributes[3].text+'\t'
        rate_of_pick = hero_attributes[4].text+'\t'
        rate_of_ban = hero_attributes[5].text+'+\t'
        three_weak_against = hero_attributes[6].find_elements_by_xpath("a/div/img")  # 这个地方前端经常维护，可能常做更改
        against_list = list()
        for against in three_weak_against:
            against_list.append(against.get_attribute('alt'))
        # against1 = three_weak_against[0].get_attribute('alt')+'\t'
        # against2 = three_weak_against[1].get_attribute('alt')+'\t'
        # against3 = three_weak_against[2].get_attribute('alt')+'\t'
        hero_result = name + layer + rate_of_victory + rate_of_pick + rate_of_ban + str(against_list) + '\n'
        result += hero_result
        print(hero_result)
    info = open(f'{version}/adc.txt', mode='w')  # 将结果写入文件
    info.write(result)
    info.close()


def get_all_sup_brief_info(browser):
    '''
    获得所有辅助英雄的基本信息
    :param browser:
    :return:
    '''
    version =get_version(browser)
    # button = browser.find_element_by_xpath("//button[text()='辅助']") # 找到辅助的按钮
    # browser.execute_script("arguments[0].click();", button)
    browser.get('https://www.op.gg/champions?region=kr&tier=platinum_plus&position=support')
    time.sleep(0.5)
    drop_scroll(browser) # 将滑条滑动到最下面
    time.sleep(0.5)
    heros = browser.find_elements_by_xpath("//table//tr") # 获得英雄表格中的每一行
    length = len(heros)
    result = ''
    for i in range(1,length,1):
        hero = heros[i]
        hero_attributes = hero.find_elements_by_xpath("td")
        name = hero_attributes[1].find_element_by_xpath("a/strong").text + '\t'
        layer = hero_attributes[2].text+'\t'
        rate_of_victory = hero_attributes[3].text+'\t'
        rate_of_pick = hero_attributes[4].text+'\t'
        rate_of_ban = hero_attributes[5].text+'+\t'
        three_weak_against = hero_attributes[6].find_elements_by_xpath("a/div/img")  # 这个地方前端经常维护，可能常做更改
        against_list = list()
        for against in three_weak_against:
            against_list.append(against.get_attribute('alt'))
        # against1 = three_weak_against[0].get_attribute('alt')+'\t'
        # against2 = three_weak_against[1].get_attribute('alt')+'\t'
        # against3 = three_weak_against[2].get_attribute('alt')+'\t'
        hero_result = name+layer+rate_of_victory+rate_of_pick+rate_of_ban+str(against_list)+'\n'
        result += hero_result
        print(hero_result)
    info = open(f'{version}/support.txt', mode='w')  # 将结果写入文件
    info.write(result)
    info.close()


def get_skill(string):
    '''
    根据字符串的信息找到对应的技能‘QWER’
    :param string: 所输入的网址字符串
    :return:
    '''
    if 'Q.' in string:
        return 'Q'
    if 'W.' in string:
        return 'W'
    if 'E.' in string:
        return 'E'
    if 'R.' in string:
        return 'R'
    return 'skill unfound'


def detail_info_from_some_position_hero(browser, some_hero, some_position = 'top'):
    '''
    从某个位置的某个英雄处开始更新信息
    :param browser:
    :param some_hero:
    :param some_position:
    :return:
    '''
    version = get_version(browser)
    list_rune = ['适应之力', '攻速', '冷缩', '适应之力', '护甲', '魔抗', '生命值', '护甲', '魔抗']  # 这个要预先设定好
    position_list = ['top','jungle','mid','adc','support']
    for position in ['top','jungle','mid','adc','support']:
        if position != some_position:
            position_list.pop(0)
        else:
            break
    for position in position_list:
        with open(version + f'/{position}.txt', encoding='gbk') as file:
            content = file.readlines()
        names = list()
        create_folder(f'{version}/{position}')
        for line in content:  # 读取top.txt，获取所有上单名称
            name = line.split('\t')[0]  # 每个上路英雄的名称
            names.append(name)  # 加入备选


        if position == some_position: # 要把之前的英雄都拿出来
            names2 = deepcopy(names)
            some_english_name = hero_dict[some_hero]
            for name in names2:
                if hero_dict[name] != some_english_name:
                    names.pop(0)
                else:
                    break
        for name in names:  # 逐个姓名爬取信息
            hero_info = ''
            english_name = str(hero_dict[name])  # 通过字典，获取该英雄中文名称对应的英文名称
            url = 'https://www.op.gg/champions/' + english_name + f'/{position}/build?region=kr&tier=platinum_plus'
            # print(url)
            browser.get(url)

            # 符文
            hero_info += '符文\n'
            rows = browser.find_elements_by_xpath("//div[@class='row']")  # 找到12行符文

            # 找到该英雄下携带的第一套大符文
            for i in [1, 2, 3, 4, 6, 7, 8]:
                row = rows[i]
                imgs = row.find_elements_by_xpath("div/div/div/img")
                for img in imgs:
                    if 'gray' not in img.get_attribute('src'):
                        fuwen_name = img.get_attribute('alt')
                        # print(fuwen_name)  # 输出符文名称
                        hero_info = hero_info + fuwen_name + '\t'

            list_order = list()  # 找到该英雄携带的第一套小符文
            for i in [9, 10, 11]:
                row = rows[i]
                imgs = row.find_elements_by_xpath("div/img")
                for img in imgs:
                    if 'gray' not in img.get_attribute('src'):
                        list_order.append(1)
                    else:
                        list_order.append(0)
            for j in range(len(list_order)):
                if list_order[j] == 1:
                    fuwen_name = list_rune[j]
                    # print(fuwen_name)  # 输出符文名称
                    hero_info = hero_info + fuwen_name + '\t'

            # 找到该英雄下携带的第二套大符文
            try:
                btn = browser.find_element_by_xpath('//*[@id="content-container"]/main/div[1]/div/div/ul/ul/li[2]')
                hero_info += '\n'
                browser.execute_script("arguments[0].click();", btn)  # 点击按钮
                # 这个位置看情况要不要设置等待时长，因为按完按钮之后可能需要加载
                rows = browser.find_elements_by_xpath("//div[@class='row']")  # 找到12行符文
                for i in [1, 2, 3, 4, 6, 7, 8]:
                    row = rows[i]
                    imgs = row.find_elements_by_xpath("div/div/div/img")
                    for img in imgs:
                        if 'gray' not in img.get_attribute('src'):
                            fuwen_name = img.get_attribute('alt')
                            # print(fuwen_name)  # 输出符文名称
                            hero_info = hero_info + fuwen_name + '\t'

                list_order = list()  # 找到该英雄携带的第二套小符文
                for i in [9, 10, 11]:
                    row = rows[i]
                    imgs = row.find_elements_by_xpath("div/img")
                    for img in imgs:
                        if 'gray' not in img.get_attribute('src'):
                            list_order.append(1)
                        else:
                            list_order.append(0)
                for j in range(len(list_order)):
                    if list_order[j] == 1:
                        fuwen_name = list_rune[j]
                        # print(fuwen_name)  # 输出符文名称
                        hero_info = hero_info + fuwen_name + '\t'
            except Exception as error:
                print(error)
                print(f'请检查{english_name}是否有第二套符文')

            # 技能加点
            try:
                hero_info += '\n\n推荐技能建设：\n'
                skills_place = browser.find_element_by_xpath(
                    '//*[@id="content-container"]/main/div[2]/div/div/div[1]/div/div[1]/div')
                skills = skills_place.find_elements_by_xpath('div/span/img')
                for skill in skills:
                    this_skill = get_skill(skill.get_attribute('src'))
                    if this_skill == 'skill unfound':
                        this_skill = skill.get_attribute('alt')
                    # print(this_skill)
                    hero_info = hero_info + this_skill + '\t'
            except Exception as error3:
                print(error3)
                print(f'请检查{english_name}是否具备技能加点')

            # 召唤师技能
            hero_info += '\n\n召唤师法术：\n'
            # 第一套召唤师技能
            d1 = browser.find_element_by_xpath(
                '//*[@id="content-container"]/aside/div[1]/div/div/div[1]/div[1]/ul/li[1]/div/img').get_attribute('alt')
            f1 = browser.find_element_by_xpath(
                '//*[@id="content-container"]/aside/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/img').get_attribute('alt')

            # 第一套相应的人数和胜率
            amounts1 = browser.find_element_by_xpath(
                '//*[@id="content-container"]/aside/div[1]/div/div/div[1]/div[2]/div[1]/small').text.replace(' 场游戏', '')
            win_rate1 = browser.find_element_by_xpath(
                '//*[@id="content-container"]/aside/div[1]/div/div/div[1]/div[2]/div[2]').text

            try:
                # 第二套召唤师技能
                d2 = browser.find_element_by_xpath(
                    '//*[@id="content-container"]/aside/div[1]/div/div/div[2]/div[1]/ul/li[1]/div/img').get_attribute('alt')
                f2 = browser.find_element_by_xpath(
                    '//*[@id="content-container"]/aside/div[1]/div/div/div[2]/div[1]/ul/li[2]/div/img').get_attribute('alt')

                # 第二套相应的人数和胜率
                amounts2 = browser.find_element_by_xpath(
                    '//*[@id="content-container"]/aside/div[1]/div/div/div[2]/div[2]/div[1]/small').text.replace(' 场游戏', '')
                win_rate2 = browser.find_element_by_xpath(
                    '//*[@id="content-container"]/aside/div[1]/div/div/div[2]/div[2]/div[2]').text

                # print(d1, f1, amounts1, win_rate1)
                hero_info = hero_info + d1 + '\t' + f1 + '\t' + amounts1 + '\t' + win_rate1 + '\n'
                # print(d2, f2, amounts2, win_rate2)
                hero_info = hero_info + d2 + '\t' + f2 + '\t' + amounts2 + '\t' + win_rate2 + '\n'
            except Exception as error2:
                print(error2)
                print(f'请检查{english_name}是否有第二套召唤师技能')

            # 反制
            hero_info += '\n反制：\n'
            counters_place = browser.find_element_by_xpath(
                '//*[@id="content-container"]/aside/div[2]/div/div/ul[1]')  # 找到反制栏
            counters = counters_place.find_elements_by_xpath('li')  # 找到对应的几个反制英雄
            for counter in counters:
                name = counter.find_element_by_xpath('a').get_attribute('href').split('target_champion=')[1]
                win_rate = counter.find_element_by_xpath('a/div[@class="win-rate"]').text
                amounts = counter.find_element_by_xpath('a/div[@class="play"]').text.replace('\n场游戏', '')
                # print(name, win_rate, amounts)
                hero_info = hero_info + hero_dict_chinese[name] + '\t' + win_rate + '\t' + amounts + '\n'

            # 初始装备
            hero_info += '\n初始装备：\n'
            try:
                first_weapon_place = browser.find_element_by_xpath(
                    '//*[@id="content-container"]/main/div[3]/div/div[1]/div[1]/table/tbody')
            except Exception as er:
                first_weapon_place = browser.find_element_by_xpath('//*[@id="content-container"]/main/div[2]/div/div[1]/div[1]/table/tbody')
            first_weapons = first_weapon_place.find_elements_by_xpath('tr')  # 找到对应的几种出门装
            for first_weapon in first_weapons:
                attributes = first_weapon.find_elements_by_xpath('td')  # 每种出门装对应的三个属性：名称、场次和胜率
                names = attributes[0].find_elements_by_xpath('div/div/div/div/img')
                names_list = list()
                for name in names:
                    names_list.append(name.get_attribute('alt'))
                # name1 = names[0].get_attribute('alt')
                # name2 = names[1].get_attribute('alt')
                amounts = attributes[1].find_element_by_xpath('small').text.replace(' 场游戏', '')
                win_rate = attributes[2].find_element_by_xpath('strong').text
                # print(names_list, amounts, win_rate)
                hero_info = hero_info + str(names_list) + '\t' + amounts + '\t' + win_rate + '\n'

            # 鞋子

            hero_info += '\n鞋子：\n'
            try:
                shoes_place = browser.find_element_by_xpath(
                '//*[@id="content-container"]/main/div[3]/div/div[1]/div[2]/table/tbody')
            except Exception as er:
                shoes_place = browser.find_element_by_xpath('//*[@id="content-container"]/main/div[2]/div/div[1]/div[2]/table/tbody')
            shoes = shoes_place.find_elements_by_xpath('tr')  # 找到对应的几种鞋子
            for shoe in shoes:
                attributes = shoe.find_elements_by_xpath('td')  # 每种鞋子对应的三个属性：名称、场次和胜率
                name = attributes[0].find_element_by_xpath('div/div/div/div/img').get_attribute('alt')
                amounts = attributes[1].find_element_by_xpath('small').text.replace(' 场游戏', '')
                win_rate = attributes[2].find_element_by_xpath('strong').text
                # print(name, amounts, win_rate)
                hero_info = hero_info + name + '\t' + amounts + '\t' + win_rate + '\n'

            # 全部出装
            try:
                hero_info += '\n推荐建设：\n'
                weapons_place = browser.find_element_by_xpath(
                    '//*[@id="content-container"]/main/div[3]/div/div[2]/div/table/tbody')
                weapons = weapons_place.find_elements_by_xpath('tr')  # 找到对应的几种出装
                for weapon in weapons:
                    attributes = weapon.find_elements_by_xpath('td')  # 每种出装对应的三个属性：名称、场次和胜率
                    names = attributes[0].find_elements_by_xpath('div/div/div/div/img')
                    names_list = list()
                    for name in names:
                        names_list.append(name.get_attribute('alt'))
                    amounts = attributes[1].find_element_by_xpath('small').text.replace(' 场游戏', '')
                    win_rate = attributes[2].find_element_by_xpath('strong').text
                    # print(names_list, amounts, win_rate)
                    hero_info = hero_info + str(names_list) + '\t' + amounts + '\t' + win_rate + '\n'
            except Exception as error4:
                print(error4)
                print(f'请检查{english_name}是否有全部出装')

            # 写入对应英雄的文件中
            create_folder(f'{version}/{position}')  # 检查是否有top文件夹，如果没有则创建
            info = open(f'{version}/{position}/{english_name}.txt', mode='w')  # 将结果写入文件,注意，
            # mode = ‘w’是覆盖写入  mode=‘a’是追加写入
            info.write(hero_info)
            info.close()