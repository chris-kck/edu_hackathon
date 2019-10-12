// Copyright (c) 2019, Runtime Terror UCT and contributors
// For license information, please see license.txt

frappe.ui.form.on('Degree Curriculum', {
	refresh: function(frm) {
    console.log("Debug: js is running");

	},

	student_number: function(frm){
	frappe.call({
    method:'degree_curr.Calculator.test',
    args: {'student_number' : frm.doc.student_number}, 
    callback: function(r) { 
        console.log(r.message);
    	console.log("Debug: py is running 1");
    	msgprint(r.message);
    	msgprint("We need to return a list");
        // set the returned value in a field
        //cur_frm.set_value("naming_series", r.message);
    	}
    })
   }

});
