// Copyright (c) 2025, Auwal Isiaku Mafindi and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student', {
    onload: function(frm) {
        fetch('/assets/school_management/nigeria_states_lgas.json')
            .then(res => res.json())
            .then(data => {
                const states = data.map(item => item.state);
                frm.set_df_property('state', 'options', [''].concat(states));
                frm.states_lgas = data;
            });
    },
    state: function(frm) {
        const selected = frm.doc.state;
        const state_data = frm.states_lgas.find(s => s.state === selected);
        const lgas = state_data ? state_data.lgas : [];
        frm.set_df_property('lga', 'options', [''].concat(lgas));
        frm.refresh_field('lga');
    }
});

