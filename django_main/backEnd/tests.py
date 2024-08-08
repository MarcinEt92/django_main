from django.test import TestCase

# Create your tests here.
import pytest
from .models import Order
from django.contrib.auth.models import User


@pytest.fixture
def new_order_factory(db):
    def create_an_order(buns: int = 0, donuts: int = 0):
        order = Order.objects.create(
            buns=buns,
            donuts=donuts
        )
        return order

    return create_an_order


@pytest.fixture
def order_1(db, new_order_factory):
    return new_order_factory(3, 4)


@pytest.fixture
def create_order(db):
    return Order.objects.create(buns=1, donuts=2)


def test_other_order_create(create_order):
    assert Order.objects.count() == 1


def test_other_next_order_create(order_1):
    assert Order.objects.count() == 1


@pytest.mark.django_db
def test_order_items(create_order):
    order = create_order
    assert order.buns == 1
    assert order.donuts == 2


@pytest.mark.django_db
def test_create_user():
    User.objects.create()
    number_of_users = User.objects.count()
    assert number_of_users == 1
