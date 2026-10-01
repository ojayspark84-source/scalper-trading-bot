from src.risk_management.martingale import Martingale


def test_martingale_is_bounded_and_resets():
    martingale = Martingale(10, 2, 2)
    assert martingale.next_stake() == 10
    martingale.record_loss()
    assert martingale.next_stake() == 20
    martingale.record_loss()
    martingale.record_loss()
    assert martingale.next_stake() == 40
    martingale.record_win()
    assert martingale.next_stake() == 10
