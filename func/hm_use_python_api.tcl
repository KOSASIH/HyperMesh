# hm_use_python_api.tcl

# Load necessary packages
package require Tcl 8.4
package require HyperMesh

# Define a procedure to use the Python API in HyperMesh
proc use_python_api {} {
    # Import the necessary Python modules
    package require python
    python::import AltairHyperWorks

    # Create a new HyperMesh session
    set session [HyperMesh::Session::create]

    # Open an existing model
    $session open_model "C:/path/to/model.hm"

    # Get the first assembly in the model
    set assembly [$session get_first_assembly]

    # Get the number of nodes in the assembly
    set num_nodes [$assembly get_num_nodes]

    # Loop through the nodes and print their IDs
    for {set i 0} {$i < $num_nodes} {incr i} {
        set node [$assembly get_node $i]
        puts "Node ID: [$node get_id]"
    }

    # Get the first component in the assembly
    set component [$assembly get_first_component]

    # Get the number of elements in the component
    set num_elements [$component get_num_elements]

    # Loop through the elements and print their IDs
    for {set i 0} {$i < $num_elements} {incr i} {
        set element [$component get_element $i]
        puts "Element ID: [$element get_id]"
    }

    # Release the session
    $session release
}

# Call the procedure to use the Python API in HyperMesh
use_python_api
