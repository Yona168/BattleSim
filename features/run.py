import subprocess
from os.path import dirname, abspath, join
from behave2cucumber import convert
import sys
from json import load, dumps

def run_tests(output_type, capture_output):
    battle_sim_folder=abspath(dirname(dirname(__file__)))
    test_folder=abspath(dirname(__file__))
    output_folder=join(battle_sim_folder, 'test_output')

    def run(args, capture):
        sys.path.insert(0, battle_sim_folder)
        if not capture:
            for arg in {'--no-capture','--no-logcapture','--no-capture-stderr'}:
                args.append(arg)
        subprocess.run(args)

    reg_json_file=join(output_folder,'json','latest_test_output.json')

    def _normal_json(capture):
        run(['behave','-f','json',
        '-o',reg_json_file], capture)

    def _cucumber(capture):
        cucumber_folder=join(output_folder, 'cucumber')
        cucumber_json_file=join(cucumber_folder,'latest_test_output_cucumber.json')
        _normal_json(capture)
        with open(reg_json_file) as old_json:
            json_text=load(old_json)
            new_json=dumps(convert(json_text))
            with open(cucumber_json_file,'w+') as new_file:
                new_file.write(new_json)

    def _allure(capture):
        run('behave -f allure_behave.formatter:AllureFormatter -o {0} {1}'.format("test_output/allure", "./features").split(), capture)

    outputs={'json':_normal_json,'cucumber':_cucumber, 'allure':_allure}
    runner=outputs.get(output_type)
    if runner is not None:
        runner(capture_output)
