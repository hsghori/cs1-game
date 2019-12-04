import yaml
import glob
from django.db.models import ObjectDoesNotExist
from api import models


def get_status(status):
    return 'A' if status == 'active' else 'I'

SEEN_MODULES = []
SEEN_GAMES = []

for file in glob.glob('./api/game_configurations/*.yaml'):
    with open(file, 'r') as f:
        module_config = yaml.load(f.read(), Loader=yaml.FullLoader)
        SEEN_MODULES.append(module_config['external_id'])
        for game_config in module_config['games']:
            SEEN_GAMES.append(game_config['external_id'])

models.GameLevelModel.objects.exclude(external_id__in=SEEN_GAMES).delete()
models.GameModuleModel.objects.exclude(external_id__in=SEEN_MODULES).delete()

for file in glob.glob('./api/game_configurations/*.yaml'):
    print(f'Compiling file: {file}')
    with open(file, 'r') as f:
        module_config = yaml.load(f.read(), Loader=yaml.FullLoader)
        try:
            module = models.GameModuleModel.objects.get(external_id=module_config['external_id'])
            module.title = module_config['title']
            module.description = module_config['description']
            module.status = get_status(module_config['status'])
            module.module_number = module_config['module_number']
            module.save()
        except ObjectDoesNotExist:
            module = models.GameModuleModel.objects.create(
                external_id=module_config['external_id'],
                title=module_config['title'],
                description=module_config['description'],
                status=get_status(module_config['status']),
                module_number=module_config['module_number']
            )
        for game_config in module_config['games']:
            games = module.games.filter(external_id=game_config['external_id'])
            if not games:
                models.GameLevelModel.objects.create(
                    external_id=game_config['external_id'],
                    title=game_config['title'],
                    description=game_config['description'],
                    status=get_status(game_config['status']),
                    module=module,
                    level_number=game_config['level_number'],
                    prompt=game_config['prompt'],
                    blocks=', '.join(game_config['blocks']),
                    inputs=game_config['inputs'],
                    num_inputs=game_config['num_inputs'],
                    list_input_size=game_config.get('list_input_size',0)
                )
            else:
                game = games[0]
                game.title = game_config['title']
                game.description = game_config['description']
                game.status = get_status(game_config['status'])
                game.level_number = game_config['level_number']
                game.prompt = game_config['prompt']
                game.blocks = ', '.join(game_config['blocks'])
                game.inputs = game_config['inputs']
                game.num_inputs = game_config['num_inputs']
                game.list_input_size = game_config.get('list_input_size',0)
                game.save()
