import csv
import os

def lecture02_01_printHeroStatus() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    hero_csv_path = os.path.join(script_dir, 'lecture02_Hero.csv')
    hero_header = []
    hero_data = []
    with open(hero_csv_path) as f:
        for line in f:
            if len(hero_header) == 0:
                hero_header = line.rstrip().split(",")
            else :
                data = line.rstrip().split(",")
                hero_data.append(data)

    for data in hero_data:
        if data[0] == '1':
            hero_name = data[1]
            hero_hp = int(data[2])
            hero_mp = int(data[3])
            hero_atk = int(data[4])
            hero_def = int(data[5])
            hero_age = int(data[6])
            print(f"{hero_name}のステータスはHP:{hero_hp},MP:{hero_mp},Atk:{hero_atk},Def:{hero_def},Age:{hero_age}")
            break

def lecture02_01_printWeaponStatus() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    weapon_csv_path = os.path.join(script_dir, 'lecture02_Weapon.csv')
    weapon_header = []
    weapon_data = []
    with open(weapon_csv_path) as f:
        reader = csv.reader(f)
        for row in reader:
            if len(weapon_header) == 0:
                weapon_header = row
            else :
                weapon_data.append(row)

    for data in weapon_data:
        if data[0] == '1':
            weapon_name = data[1]
            weapon_hp = int(data[2])
            weapon_mp = int(data[3])
            weapon_atk = int(data[4])
            weapon_def = int(data[5])
            weapon_age = int(data[6])
            print(f"{weapon_name}のステータスはHP:{weapon_hp},MP:{weapon_mp},Atk:{weapon_atk},Def:{weapon_def},Age:{weapon_age}")
            break

def lecture02_01_printHeroStatusWithWeapon() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    hero_csv_path = os.path.join(script_dir, 'lecture02_Hero.csv')
    weapon_csv_path = os.path.join(script_dir, 'lecture02_Weapon.csv')
    
    # Heroデータを読み込む
    hero_header = []
    hero_data = []
    with open(hero_csv_path) as f:
        for line in f:
            if len(hero_header) == 0:
                hero_header = line.rstrip().split(",")
            else :
                data = line.rstrip().split(",")
                hero_data.append(data)
    
    for data in hero_data:
        if data[0] == '1':
            hero_name = data[1]
            hero_hp = int(data[2])
            hero_mp = int(data[3])
            hero_atk = int(data[4])
            hero_def = int(data[5])
            hero_age = int(data[6])
            hero_weapon = data[7]
            break
    
    # 武器データを読み込む
    weapon_header = []
    weapon_data = []
    with open(weapon_csv_path) as f:
        reader = csv.reader(f)
        for row in reader:
            if len(weapon_header) == 0:
                weapon_header = row
            else :
                weapon_data.append(row)
    
    for data in weapon_data:
        if data[0] == hero_weapon:
            weapon_name = data[1]
            weapon_hp = int(data[2])
            weapon_mp = int(data[3])
            weapon_atk = int(data[4])
            weapon_def = int(data[5])
            weapon_age = int(data[6])
            break
    
    # ステータス情報を出力する
    print(f"{weapon_name}を装備した{hero_name}のステータスは" +
        f"HP:{hero_hp+weapon_hp}," +
        f"MP:{hero_mp+weapon_mp}," +
        f"Atk:{hero_atk+weapon_atk}," +
        f"Def:{hero_def+weapon_def}," +
        f"Age:{hero_age+weapon_age}")

if __name__ == '__main__':
    lecture02_01_printHeroStatus()
    lecture02_01_printWeaponStatus()
    lecture02_01_printHeroStatusWithWeapon()
