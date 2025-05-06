// Copyright (c) 2025, Auwal Isiaku Mafindi and contributors
// For license information, please see license.txt

// frappe.ui.form.on("School Class", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('School Class', {
//    class_level: function(frm) {
//        // Clear fields when level changes
        //frm.set_value('class_arm', '');
  //      frm.set_value('full_class_name', '');
//
  //      if (frm.doc.class_level) {
    //        frappe.call({
      //          method: 'school_management.school_management.doctype.school_class.school_class.get_class_arms',
//                args: {
  //                  class_level: frm.doc.class_level
   //             },
    //            callback: function(r) {
     //               if (!r.exc && r.message) {
       //                 frm.set_df_property('class_arm', 'options', r.message.join('\n'));
            //        }
          //      }
        //    });
      //  }
    //},
    class_arm: function(frm) {
       if (frm.doc.class_level && frm.doc.class_arm) {
            frm.set_value('full_class_name', 
             `${frm.doc.class_level} ${frm.doc.class_arm}`);
      }
    }
});
