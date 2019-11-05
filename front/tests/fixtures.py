import pytest


@pytest.fixture(scope='function')
def get_client(client):
    return client


@pytest.fixture(scope='function')
def create_user(django_user_model):
    username = "testuser"
    password = "testpassword"
    django_user_model.objects.create_user(username=username, password=password)

    return username, password


@pytest.fixture(scope='function')
def load_game_data(db):

    import compile_configs

    return True


@pytest.fixture(scope='function')
def logged_in_client(create_user, client):
    username, password = create_user
    client.login(username=username, password=password)

    return client
