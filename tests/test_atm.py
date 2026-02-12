from ATM_Practice import ATM, Account, Technician, Administration
import pytest


# ATM CLASS TESTS

def test_account_string_representation():

    nico = Account(_pin=2026, name="Nico", _balance=0, _active=True)
    blocked_user = Account(_pin=2026, name="blocked", _balance=0, _active=False)

    assert str(nico) == "You are Nico, your account is currently online"
    assert "currently disabled" in str(blocked_user)


def test_cash_inventory_is_protected():
    cajero = ATM("New York", _cash_inventory=1000)

    assert cajero.cash_inventory == 1000
    with pytest.raises(AttributeError):
        cajero.cash_inventory = 5000

def test_initial_balance():

    nico = Account(_pin=2026, name="Nick", _balance=500, _active=True)
    assert nico.balance == 500

def test_change_power_status():

    atm = ATM("New Jersey", 10000, _is_active=True, _admin_key= 129)
    atm.change_power_status(129, new_status= False)

    assert atm._is_active == False

def test_withdraw_balance():

    cajero = ATM("New York", _admin_key = 1234)

    nico = Account(_pin=2026, name="Nick", _balance=40000, _active=True)

    cajero.withdraw(nico, 1, 2026)

    assert nico.balance == 39999

def test_atm_reload():

    cajero = ATM("New York", _admin_key = 1234)

    jorge = Technician("Jorge", 1234)

    jorge.reload_atm(cajero, 1)

    assert cajero.cash_inventory == 500001

def test_block_user_from_atm():
    cajero = ATM("New York", _admin_key = 1234)
    Johnny = Administration("Johnny Guitar", 1234)
    nico = Account(_pin=2026, name="Nick", _balance=0, _active=True)
    
    Johnny.block_user(cajero, nico)
    assert nico.active is False

def test_how_many_atm():
    ATM.number_of_atms = 0 #manual reset

    cajero = ATM("New York", _admin_key = 1234)
    dublin_ATM = ATM("Dublin", _admin_key= 3950)
    
    assert ATM.how_many_atm() == 2
    

#  Technician Class tests

def test_turn_off_and_on_atm():
    
    box = ATM("Colorado", 1000, _admin_key = 130)
    george = Technician("George", _key=130)

    george.turn_off_atm(box)

    assert box.is_active == False

    george.turning_on_atm(box)
    
    assert box.is_active == True


# Account class tests
def test_how_many_users():

    Account.number_of_accounts = 0

    nico = Account(_pin=2026, name="Nick", _balance=0, _active=True)

    assert Account.how_many_accounts() == 1


def test_checkfund():

    nico = Account(_pin=2026, name="Nick", _balance=10, _active=True)

    assert nico.check_funds(10) == True
    assert nico.check_funds(11) == False
def test_deduct():

    nico = Account(_pin=2026, name="Nick", _balance=10, _active=True)
    
    nico.deduct(10)

    assert nico.balance == 0



