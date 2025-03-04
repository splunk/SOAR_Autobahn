"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'cf_local_pov_set_event_owner_to_current_py3_1' block
    cf_local_pov_set_event_owner_to_current_py3_1(container=container)

    return

@phantom.playbook_block()
def cf_local_pov_set_event_owner_to_current_py3_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("cf_local_pov_set_event_owner_to_current_py3_1() called")

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

    phantom.custom_function(custom_function="SOAR_Autobahn/POV_set_event_owner_to_current_py3", parameters=parameters, name="cf_local_pov_set_event_owner_to_current_py3_1", callback=pov_get_current_task_py3_5)

    return


@phantom.playbook_block()
def decision_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("decision_1() called")

    # check for 'if' condition 1
    found_match_1 = phantom.decision(
        container=container,
        conditions=[
            ["pov_get_current_task_py3_5:custom_function_result.data.status", "==", "failed"]
        ],
        delimiter=None)

    # call connected blocks if condition 1 matched
    if found_match_1:
        add_comment_1(action=action, success=success, container=container, results=results, handle=handle)
        return

    # check for 'else' condition 2
    set_status_2(action=action, success=success, container=container, results=results, handle=handle)

    return


@phantom.playbook_block()
def add_comment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("add_comment_1() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.comment(container=container, comment="Unable to get tasks for container. - Please check.")

    return


@phantom.playbook_block()
def set_status_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("set_status_2() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.set_status(container=container, status="open")

    return


@phantom.playbook_block()
def pov_get_current_task_py3_5(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, loop_state_json=None, **kwargs):
    phantom.debug("pov_get_current_task_py3_5() called")

    id_value = container.get("id", None)
    cf_local_pov_set_event_owner_to_current_py3_1__result = phantom.collect2(container=container, datapath=["cf_local_pov_set_event_owner_to_current_py3_1:custom_function_result.data.currentOwner"])

    cf_local_pov_set_event_owner_to_current_py3_1_data_currentowner = [item[0] for item in cf_local_pov_set_event_owner_to_current_py3_1__result]

    parameters = []

    parameters.append({
        "container": id_value,
        "currentOwner": cf_local_pov_set_event_owner_to_current_py3_1_data_currentowner,
    })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.custom_function(custom_function="SOAR_Autobahn/POV_get_current_task_py3", parameters=parameters, name="pov_get_current_task_py3_5", callback=decision_1)

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