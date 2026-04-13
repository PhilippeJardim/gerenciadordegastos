import pytest
from django.utils import timezone
from gastos.models import Despesa

@pytest.mark.django_db
def test_criar_despesa():
    """Testa a criação de uma despesa."""
    despesa = Despesa.objects.create(
        descricao="Mensalidade Escolar",
        valor=1500,
        categoria="educacao",
        data=timezone.now().date(),
    )
    assert despesa.pk is not None

@pytest.mark.django_db
def test_str_despesa():
    """Testa a representação em string de uma despesa."""
    despesa = Despesa(descricao="Transporte", valor=15.00)
    assert str(despesa) == "Transporte - R$ 15.00"

@pytest.mark.django_db
def test_listagem_despesa():
    """Testa a listagem de despesas."""
    Despesa.objects.create(
    descricao="Cinema",
    valor=30.00,
    categoria="lazer",
    data=timezone.now().date()
)
    Despesa.objects.create(
    descricao="Supermercado",
    valor=100.00,
    categoria="alimentacao",
    data=timezone.now().date()
)

    despesas = Despesa.objects.all()
    assert despesas.count() == 2