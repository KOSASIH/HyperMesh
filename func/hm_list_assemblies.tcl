# hm_list_assemblies.tcl

# Load necessary packages
package require Tcl 8.4
package require HyperMesh

# Define a procedure to list all assemblies in the model
proc list_assemblies {} {
    # Get the current design
    set design [DboSession_GetDesignAndSchematics]

    # Get all assemblies in the design
    set assemblies [$design GetAssemblies]

    # Print the name of each assembly
    foreach assembly $assemblies {
        puts "Assembly: $assembly"
    }

    # Export the list of assemblies to a file
    set output_file [file join [pwd] "assembly_list.txt"]
    set file_id [open $output_file "w"]
    puts $file_id "List of assemblies in the current design:"
    foreach assembly $assemblies {
        puts $file_id "Assembly: $assembly"
    }
    close $file_id

    # Create a report with the list of assemblies
    set report_name [file join [pwd] "assembly_list_report.hwr"]
    hm_create_report -name $report_name -title "Assembly List Report"
    hm_add_module_to_report -name $report_name -module "Model Info"
    hm_run_report -name $report_name

    # Open the report in a web browser
    set report_url [file join [pwd] "reports/$report_name.html"]
    exec firefox $report_url

    # Create a graphical visualization of the assemblies
    set graph_name [file join [pwd] "assembly_list_graph.gph"]
    hm_create_graph -name $graph_name -title "Assembly List Graph"
    hm_add_node_to_graph -name $graph_name -node "Assemblies"
    hm_add_edge_to_graph -name $graph_name -edge "Assembly List" -source "Assemblies" -target $assemblies
    hm_run_graph -name $graph_name

    # Open the graph in a web browser
    set graph_url [file join [pwd] "graphs/$graph_name.html"]
    exec firefox $graph_url

    # Add custom properties to all parts in the design
    set part_properties [list]
    foreach assembly $assemblies {
        set parts [$assembly GetParts]
        foreach part $parts {
            # Add the part to the list of part properties
            lappend part_properties [list $part "PartVersion" "1.1"]
        }
    }

    # Add the custom properties to the parts
    foreach part_prop $part_properties {
        set part [lindex $part_prop 0]
        set prop_name [lindex $part_prop 1]
        set prop_value [lindex $part_prop 2]
        $part SetEffectivePropStringValue $prop_name $prop_value
    }

    # Save the design with the new properties
    $design Save
}

# Call the procedure to list all assemblies in the current design
list_assemblies
