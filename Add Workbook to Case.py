"""
This workbook, runs on all events, looking for container names and labels with known workbooks that are used in the POV, and automatically attaches the workbook to save an analyst doing it manually.
"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


################################################################################
## Global Custom Code Start
################################################################################

################################################################################
## Global Custom Code End
################################################################################

@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'pov_add_workbook_py3_2' block
    pov_add_workbook_py3_2(container=container)

    return

@phantom.playbook_block()
def pov_add_workbook_py3_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("pov_add_workbook_py3_2() called")

    id_value = container.get("id", None)

    parameters = []

    parameters.append({
        "container": id_value,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="SOAR_Autobahn/POV_Add_Workbook_py3", parameters=parameters, name="pov_add_workbook_py3_2")

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return