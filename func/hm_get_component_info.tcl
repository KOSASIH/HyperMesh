# hm_get_component_info.tcl

# Load necessary packages
package require Tcl 8.4
package require HyperMesh

# Define a procedure to get component information
proc get_component_info {} {
    # Get the current design
    set design [DboSession_GetDesignAndSchematics]

    # Get all components in the design
    set components [$design GetComponents]

    # Print the name and type of each component
    foreach component $components {
        set name [$component GetName]
        set type [$component GetType]
        puts "Component: $name, Type: $type"

        # Get the nodes of the component
        set nodes [$component GetNodes]

        # Print the ID and coordinates of each node
        puts "Nodes:"
        foreach node $nodes {
            set id [$node GetID]
            set x [$node GetX]
            set y [$node GetY]
            set z [$node GetZ]
            puts "Node: $id, Coordinates: ($x, $y, $z)"
        }

        # Get the elements of the component
        set elements [$component GetElements]

        # Print the ID and type of each element
        puts "Elements:"
        foreach element $elements {
            set id [$element GetID]
            set type [$element GetType]
            puts "Element: $id, Type: $type"
        }
    }

    # Export the component information to a file
    set output_file [file join [pwd] "component_info.txt"]
    set file_id [open $output_file "w"]
    puts $file_id "List of components in the current design:"
    foreach component $components {
        set name [$component GetName]
        set type [$component GetType]
        puts $file_id "Component: $name, Type: $type"

        # Get the nodes of the component
        set nodes [$component GetNodes]

        # Write the ID and coordinates of each node to the file
        puts $file_id "Nodes:"
        foreach node $nodes {
            set id [$node GetID]
            set x [$node GetX]
            set y [$node GetY]
set z [$node GetZ]
            puts $file_id "Node: $id, Coordinates: ($x, $y, $z)"
        }

        # Get the elements of the component
        set elements [$component GetElements]

        # Write the ID and type of each element to the file
        puts $file_id "Elements:"
        foreach element $elements {
            set id [$element GetID]
            set type [$element GetType]
            puts $file_id "Element: $id, Type: $type"
        }
    }
    close $file_id

    # Create a report with the component information
    set report_name [file join [pwd] "component_info_report.hwr"]
    hm_create_report -name $report_name -title "Component Information Report"
    hm_add_module_to_report -name $report_name -module "Model Info"
    hm_run_report -name $report_name

    # Open the report in a web browser
    set report_url [file join [pwd] "reports/$report_name.html"]
    exec firefox $report_url

    # Create a graphical visualization of the components
    set graph_name [file join [pwd] "component_info_graph.gph"]
    hm_create_graph -name $graph_name -title "Component Information Graph"
    hm_add_node_to_graph -name $graph_name -node "Components"
    hm_add_edge_to_graph -name $graph_name -edge "Component List" -source "Components" -target $components
    hm_run_graph -name $graph_name

    # Open the graph in a web browser
    set graph_url [file join [pwd] "graphs/$graph_name.html"]
    exec firefox $graph_url

    # Add custom properties to all components in the design
    set component_properties [list]
    foreach component $components {
        set name [$component GetName]
        set type [$component GetType]
        lappend component_properties [list $component "ComponentName" $name "ComponentType" $type]
    }

    # Add the custom properties to the components
    foreach comp_prop $component_properties {
        set component [lindex $comp_prop 0]
        set prop_name [lindex $comp_prop 1]
        set prop_value [lindex $comp_prop 2]
        $component SetEffectivePropStringValue $prop_name $prop_value
    }

    # Save the design with the new properties
    $design Save
}

# Call the procedure to get component information
get_component_info
