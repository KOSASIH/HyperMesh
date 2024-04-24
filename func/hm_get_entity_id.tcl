# hm_get_entity_id.tcl

# Get the entity ID numbers on a mark

# Check if the user has selected any entities
if {[llength $args] == 0} {
    puts "Usage: hm_get_entity_id mark_name"
    return
}

# Get the mark name from the command line arguments
set mark_name [lindex $args 0]

# Check if the mark exists
if {[catch {set mark_id [hm_get_mark_id $mark_name]}]} {
    puts "Error: Mark '$mark_name' not found"
    return
}

# Get the entity ID numbers on the mark
set entity_ids [hm_get_entity_ids -mark_id $mark_id]

# Print the entity ID numbers
puts "Entity IDs on mark '$mark_name': $entity_ids"

# Export the entity ID numbers to a file
set output_file [file join [pwd] "entity_ids.txt"]
set file_id [open $output_file "w"]
puts $file_id $entity_ids
close $file_id

# Visualize the entity ID numbers
set entity_set [hm_create_entity_set -entity_ids $entity_ids]
hm_display_entity_set $entity_set

# Create a report with the entity ID numbers
set report_name [file join [pwd] "entity_ids_report.hwr"]
hm_create_report -name $report_name -title "Entity IDs Report"
hm_add_module_to_report -name $report_name -module "Model Info"
hm_run_report -name $report_name

# Open the report in a web browser
set report_url [file join [pwd] "reports/$report_name.html"]
exec firefox $report_url
