from Item import Item

item = Item("Wooden Sword", "This is a wooden sword!", 10)

def test_Damage():
    assert item.getDamage() == 10
    
def test_UpdateDamage():
    item.setDamage(15)				# 15
    item.setDot(2, 10)				# 20
    assert item.getDamage() == 35
    
def test_criticalHitDamage():
    assert item.criticalHit() == 70