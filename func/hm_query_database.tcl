# hm_query_database.tcl

# Load necessary packages
package require Tcl 8.4
package require HyperMesh

# Define a procedure to query the database
proc query_database {} {
    # Get the current design
    set design [DboSession_GetDesignAndSchematics]

    # Get all entities in the design
    set entities [$design GetEntities]

    # Print the ID and type of each entity
    puts "Entities:"
    foreach entity $entities {
        set id [$entity GetID]
        set type [$entity GetType]
        puts "Entity: $id, Type: $type"

        # Get the values of all properties for the entity
        set prop_values [$entity GetEffectivePropValues]

        # Print the name and value of each property
        puts "Properties:"
        foreach prop_value $prop_values {
            set prop_name [$prop_value GetName]
            set prop_value [$prop_value GetValue]
            puts "Property: $prop_name, Value: $prop_value"
        }
    }

    # Export the entity information to a file
    set output_file [file join [pwd] "entity_info.txt"]
    set file_id [open $output_file "w"]
    puts $file_id "List of entities in the current design:"
    foreach entity $entities {
        set id [$entity GetID]
        set type [$entity GetType]
        puts $file_id "Entity: $id, Type: $type"

        # Get the values of all properties for the entity
        set prop_values [$entity GetEffectivePropValues]

        # Write the name and value of each property to the file
        puts $file_id "Properties:"
        foreach prop_value $prop_values {
            set prop_name [$prop_value GetName]
            set prop_value [$prop_value GetValue]
            puts $file_id "Property: $prop_name, Value: $prop_value"
        }
    }
    close $file_id

    # Create a report with the entity information
    set report_name [file join [pwd] "entity_info_report.hwr"]
    hm_create_report -name $report_name -title "Entity Information Report"
    hm_add_module_to_report -name $report_name -module "Model Info"
    hm_run_report -name $report_name

    # Open the report in a web browser
    set report_url [file join [pwd] "reports/$report_name.html"]
    exec firefox $report_url

    # Create a graphical visualization of the entities
    set graph_name [file join [pwd] "entity_info_graph.gph"]
    hm_create_graph -name $graph_name -title "Entity Information Graph"
    hm_add_node_to_graph -name $graph_name -node "Entities"
    hm_add_edge_to_graph -name $graph_name -edge "Entity List" -source "Entities" -target $entities
    hm_run_graph -name $graph_name

    # Open the graph in a web browser
    set graph_url [file join [pwd] "graphs/$graph_name.html"]
    exec firefox $graph_url

    # Add custom properties to all entities in the design
    set entity_properties [list]
    foreach entity $entities {
        set id [$entity GetID]
        lappend entity_properties [list $entity "EntityID" $id]
    }

    # Add the custom properties to the entities
    foreach entity_prop $entity_properties {
        set entity [lindex $entity_prop 0]
        set prop_name [lindex $entity_prop 1]
        set prop_value [lindex $entity_prop 2]
        $entity SetEffectivePropStringValue $prop_name $prop_value
    }

    # Save the design with the new properties
    $design Save
}

. 
=====================
