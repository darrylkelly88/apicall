import requests
import json
from requests.structures import CaseInsensitiveDict

def apicall():

                url = "https://aap.redhat.tdbsc.co.uk/api/v2/workflow_job_templates/13/launch"

                PAT_token = "Bearer nsoNIspjEuAo8dwt2ZPYJqBXomADcC"

                headers = CaseInsensitiveDict()
                headers["Authorization"] = PAT_token
                headers["Content-Type"] = "application/json"
                data = """

                {

                    "ask_limit_on_launch": false,

                    "ask_scm_branch_on_launch": false

                }

                """

                resp = requests.post(url, headers=headers, data=data, verify=False)
                data = resp.json()
                print(data)
                print(resp.status_code)


apicall()
