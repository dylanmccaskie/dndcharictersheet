
def makesheet():
    name = input("what is your charicters name")
    charicterclass = input("what is your charicters class")
    background = input("what is your charicters background")
    race = input("what is your charicters race ")
    allingemnt = input("what is your charicters allingment")
    experiance = int(input("how much experiance dose your charicter have"))
    strength = int(input("what is your charicters strength score"))
    dexterity = int(input("what is your charicters dexterity score"))
    constitution = int(input("what is your charicters constitution score"))
    intellegance = int(input("what is your charicters intelegance score"))
    wisdom = int(input("what is your charicters wisdom score"))
    charistma = int(input("what is your charicters charisma score"))
    skills = {
        "Athletics" : False,
        "Acrobatics" : False,
        "Sleight of Hand" : False,
        "Stealth" : False,
        "Arcana" : False,
        "History" : False,
        "Investigation" : False,
        "Nature" : False,
        "Religion" : False,
        "Animal Handling"  : False,
        "Insight": False,
        "Medicine" : False,
        "Perception" : False,
        "Survival" : False,
        "Deception" : False,
        "Intimidation" : False,
        "Performance" : False,
        "Persuasion" : False 
    }
    numberofskills = input("how many skills is your charictor proficent in")
    for i in range(numberofskills):
        skilltoupdate = input("please enter a skill your charicter is proficent in")
        skills.update(skilltoupdate = True)
        
    saves = {
        "strength" : False,
        "dexterity" : False,
        "constitution" : False,
        "intellegance" : False,
        "Wisdom" : False,
        "charisma" : False,
    }
    numberofsaves = input("how many saves is your charictor proficent in")
    for i in range(numberofsaves):
        savetoupdate = input("please enter a save your charicter is proficent in")
        saves.update(savetoupdate = True)

    proficencysandlanguages = input("please list all other proficenys and languages your charicter has")
    equipment = input("please list all your charicters equipment") 
    personalitytriats = input("what is your charicters personality trait")
    ideals = input("what are your charicters ideals")
    bonds = input("what are your charicters bonds") 
    flaws = input("what are your charicters flaws")
    ac = int(input("what is your charicters armour class"))
    inititive = int(input("what is your charicters inititive"))
    speed = int(input("what is your charicters speed"))
    maxhp = int(input("what is your charicters max hp"))
    numberhitdice = int(input("how many hit dce dose your charicter have"))
    typehitdice = int(input("what die is your charicters hit dice"))
    pp = int(input("how many platinum pieces dose your charicter have"))
    gp = int(input("how many gold pieces dose your charicter have"))
    ep = int(input("how many electrum pieces dose your charicter have"))
    sp = int(input("how many silver pieces dose your charicter have"))
    cp = int(input("how many copper pieces dose your charicter have"))
    



def main():
    makesheet()


if __name__ == '__main__':
    main()