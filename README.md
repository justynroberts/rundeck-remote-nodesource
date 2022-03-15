
# rundeck-remote-nodesource

## Sample code for running a remote nodesource

A quick example of how to parse an existing node source .yaml file, convert to json and push via the API to a project.
This can be run from the runner, (Subject to connectivity, of course)

**Installation**
Will require python3 with the following modules deployed:

  PyYAML                 

Also listed in the requirements.txt

**Format**

    nodepost.py [path to yaml] [host] [apitoken] [index] [project] 

> There is currently no error checking here, so its important to get
> this format correct.

**Parameters**

`host` : eg. myenv.rundeck.cloud

`apitoken`: A valid Rundeck API token

`index`: The index of the node source (tested against the simple node source).

`project`: Project Name

A typical command line might be:

    nodepost.py /nodes/nodes.yaml myenv.rundeck.cloud aaa1112223333 2 Development

Would pull everything in nodes.yaml to index 2 (Simple Node Wizard) in the development project.

**Important**
 - This has only been tested against a simple node wizard.If you dont have one, you will need to create one
 - This will overwrite EVERYTHING in the node list for that index. Consider it a
                 complete replacement for the particular node source.

Supplied as a sample. As Is.
