# hm_get_node_values.tcl

# Load necessary packages
package require Tcl 8.4
package require HyperMesh

# Define a procedure to get node values
proc get_node_values {} {
    # Get the current design
    set design [DboSession_GetDesignAndSchematics]

    # Get all nodes in the design
    set nodes [$design GetNodes]

    # Print the ID and coordinates of each node
    puts "Nodes:"
    foreach node $nodes {
        set id [$node GetID]
        set x [$node GetX]
        set y [$node GetY]
        set z [$node GetZ]
        puts "Node: $id, Coordinates: ($x, $y, $z)"

        # Get the values of all properties for the node
        set prop_values [$node GetEffectivePropValues]

        # Print the name and value of each property
        puts "Properties:"
        foreach prop_value $prop_values {
            set prop_name [$prop_value GetName]
            set prop_value [$prop_value GetValue]
            puts "Property: $prop_name, Value: $prop_value"
        }
    }

    # Export the node values to a file
    set output_file [file join [pwd] "node_values.txt"]
    set file_id [open $output_file "w"]
    puts $file_id "List of nodes in the current design:"
    foreach node $nodes {
        set id [$node GetID]
        set x [$node GetX]
        set y [$node GetY]
        set z [$node GetZ]
        puts $file_id "Node: $id, Coordinates: ($x, $y, $z)"

        # Get the values of all properties for the node
        set prop_values [$node GetEffectivePropValues]

        # Write the name and value of each property to the file
        puts $file_id "Properties:"
        foreach prop_value $prop_values {
            set prop_name [$prop_value GetName]
            set prop_value [$prop_value GetValue]
            puts $file_id "Property: $prop_name, Value: $prop_value"
        }
    }
    close $file_id

    # Create a report with the node values
    set report_name [file join [pwd] "node_values_report.hwr"]
    hm_create_report -name $report_name -title "Node Values Report"
    hm_add_module_to_report -name $report_name -module "Model Info"
    hm_run_report -name $report_name

    # Open the report in a web browser
    set report_url [file join [pwd] "reports/$report_name.html"]
    exec firefox $report_url

    # Create a graphical visualization of the nodes
    set graph_name [file join [pwd] "node_values_graph.gph"]
    hm_create_graph -name $graph_name -title "Node Values Graph"
    hm_add_node_to_graph -name $graph_name -node "Nodes"
    hm_add_edge_to_graph -name $graph_name -edge "Node List" -source "Nodes" -target $nodes
    hm_run_graph -name $graph_name

    # Open the graph in a web browser
    set graph_url [file join [pwd] "graphs/$graph_name.html"]
    exec firefox $graph_url

    # Add custom properties to all nodes in the design
    set node_properties [list]
    foreach node $nodes {
        set id [$node GetID]
        lappend node_properties [list $node "NodeID" $id]
    }

    # Add the custom properties to the nodes
    foreach node_prop $node_properties {
        set node [lindex $node_prop 0]
        set prop_name [lindex $node_prop 1]
        set prop_value [lindex $node_prop 2]
        $node SetEffectivePropStringValue $prop_name $prop_value
    }

    # Save the design with the new properties
    $design Save
}

# Call the procedure to get node values
get_node_values
