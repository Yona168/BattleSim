import subprocess
from os.path import dirname,join
def run_tests():
    battle_sim_folder=dirname(dirname(__file__))
    print(battle_sim_folder)
    subprocess.run('behave', cwd=battle_sim_folder)
