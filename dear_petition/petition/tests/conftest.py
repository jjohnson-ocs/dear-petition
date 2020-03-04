import pytest

from dear_petition.petition.tests.factories import BatchFactory, CIPRSRecordFactory


@pytest.fixture
def batch():
    yield BatchFactory()


@pytest.fixture
def record1(batch):
    yield CIPRSRecordFactory(batch=batch, label=batch.label)


@pytest.fixture
def record2(batch):
    yield CIPRSRecordFactory(batch=batch, label=batch.label)