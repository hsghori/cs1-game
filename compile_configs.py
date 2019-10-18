import yaml
import glob
from django.db.models import ObjectDoesNotExist
from api import models


def get_status(status):
    return 'A' if status == 'active' else 'I'


for file in glob.glob('./api/game_configurations/*.yaml'):
    print(f'Compiling file: {file}')
    with open(file, 'r') as f:
        module_config = yaml.load(f.read(), Loader=yaml.FullLoader)
        try:
            module = models.GameModuleModel.objects.get(external_id=module_config['external_id'])
            module.title = module_config['title']
            module.description = module_config['description']
            module.status = get_status(module_config['status'])
            module.save()
        except ObjectDoesNotExist:
            module = models.GameModuleModel.objects.create(
                external_id=module_config['external_id'],
                title=module_config['title'],
                description=module_config['description'],
                status=get_status(module_config['status'])
            )
        for game_config in module_config['games']:
            games = module.games.filter(external_id=game_config['external_id'])
            if not games:
                models.GameLevelModel.objects.create(
                    external_id=game_config['external_id'],
                    title=game_config['title'],
                    description=game_config['description'],
                    status=get_status(game_config['status']),
                    module=module
                )
            else:
                game = games[0]
                game.title = game_config['title']
                game.description = game_config['description']
                game.status = get_status(game_config['status'])
                game.save()
