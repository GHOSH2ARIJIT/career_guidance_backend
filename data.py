streams = [
    {
        'id': 1,
        'name': 'Commerce'
    },
    {
        'id': 2,
        'name': 'Science'
    },
    {
        'id': 3,
        'name': 'Arts'
    }
]

subjects = [
    {'id': 1, 'name': 'Accounting'},
    {'id': 2, 'name': 'Business Studies'},
    {'id': 3, 'name': 'Economics'},
    {'id': 4, 'name': 'Entrepreneurship'},
    {'id': 5, 'name': 'Marketing'},
    {'id': 6, 'name': 'Finance'},
    {'id': 7, 'name': 'Taxation'},
    {'id': 8, 'name': 'Physics'},
    {'id': 9, 'name': 'Chemistry'},
    {'id': 10, 'name': 'Biology'},
    {'id': 11, 'name': 'Mathematics'},
    {'id': 12, 'name': 'Computer Science'},
    {'id': 13, 'name': 'Environmental Science'},
    {'id': 14, 'name': 'Statistics'},
    {'id': 15, 'name': 'History'},
    {'id': 16, 'name': 'Political Science'},
    {'id': 17, 'name': 'Psychology'},
    {'id': 18, 'name': 'Sociology'},
    {'id': 19, 'name': 'Philosophy'},
    {'id': 20, 'name': 'English Literature'},
    {'id': 21, 'name': 'Fine Arts'}
]

combo = [
    {'id': 1, 'name': 'Physics, Chemistry + Mathematics'},  
    {'id': 2, 'name': 'Physics, Chemistry + Biology'},
    {'id': 3, 'name': 'Physics, Chemistry + Mathematics + Biology'},
    {'id': 4, 'name': 'Computer Science + Physics, Chemistry + Mathematics'},
    {'id': 5, 'name': 'Environmental Science + Physics, Chemistry + Biology'},
    {'id': 6, 'name': 'Statistics + Mathematics + Computer Science'},
    {'id': 7, 'name': 'Accounting + Business Studies + Economics'},
    {'id': 8, 'name': 'Finance + Marketing + Entrepreneurship'},
    {'id': 9, 'name': 'Business Studies + Economics + Mathematics'},
    {'id': 10, 'name': 'Taxation + Accounting + Business Law'},
    {'id': 11, 'name': 'History + Political Science + Sociology'},
    {'id': 12, 'name': 'Psychology + Philosophy + English Literature'},
    {'id': 13, 'name': 'Fine Arts + History + English Literature'},
    {'id': 14, 'name': 'Political Science + Economics + Geography'},
    {'id': 15, 'name': 'Sociology + Psychology + Environmental Science'}
]

subject_combo = [
    {'id': 1, 'combo_id': 1, 'subject_id': 8},
    {'id': 2, 'combo_id': 1, 'subject_id': 9},
    {'id': 3, 'combo_id': 1, 'subject_id': 11},
    {'id': 4, 'combo_id': 2, 'subject_id': 8},
    {'id': 5, 'combo_id': 2, 'subject_id': 9},
    {'id': 6, 'combo_id': 2, 'subject_id': 10},
    {'id': 7, 'combo_id': 3, 'subject_id': 8},
    {'id': 8, 'combo_id': 3, 'subject_id': 9},
    {'id': 9, 'combo_id': 3, 'subject_id': 11},
    {'id': 10, 'combo_id': 3, 'subject_id': 10},
    {'id': 11, 'combo_id': 4, 'subject_id': 12},
    {'id': 12, 'combo_id': 4, 'subject_id': 8},
    {'id': 13, 'combo_id': 4, 'subject_id': 9},
    {'id': 14, 'combo_id': 4, 'subject_id': 11},
    {'id': 15, 'combo_id': 5, 'subject_id': 13},
    {'id': 16, 'combo_id': 5, 'subject_id': 8},
    {'id': 17, 'combo_id': 5, 'subject_id': 9},
    {'id': 18, 'combo_id': 5, 'subject_id': 10},
    {'id': 19, 'combo_id': 6, 'subject_id': 14},
    {'id': 20, 'combo_id': 6, 'subject_id': 11},
    {'id': 21, 'combo_id': 6, 'subject_id': 12},
    {'id': 22, 'combo_id': 7, 'subject_id': 1},
    {'id': 23, 'combo_id': 7, 'subject_id': 2},
    {'id': 24, 'combo_id': 7, 'subject_id': 3},
    {'id': 25, 'combo_id': 8, 'subject_id': 6},
    {'id': 26, 'combo_id': 8, 'subject_id': 5},
    {'id': 27, 'combo_id': 8, 'subject_id': 4},
    {'id': 28, 'combo_id': 9, 'subject_id': 2},
    {'id': 29, 'combo_id': 9, 'subject_id': 3},
    {'id': 30, 'combo_id': 9, 'subject_id': 11},
    {'id': 31, 'combo_id': 10, 'subject_id': 7},
    {'id': 32, 'combo_id': 10, 'subject_id': 1},
    {'id': 33, 'combo_id': 10, 'subject_id': 2},
    {'id': 34, 'combo_id': 11, 'subject_id': 15},
    {'id': 35, 'combo_id': 11, 'subject_id': 16},
    {'id': 36, 'combo_id': 11, 'subject_id': 18},
    {'id': 37, 'combo_id': 12, 'subject_id': 17},
    {'id': 38, 'combo_id': 12, 'subject_id': 19},
    {'id': 39, 'combo_id': 12, 'subject_id': 20},
    {'id': 40, 'combo_id': 13, 'subject_id': 21},
    {'id': 41, 'combo_id': 13, 'subject_id': 15},
    {'id': 42, 'combo_id': 13, 'subject_id': 20},
    {'id': 43, 'combo_id': 14, 'subject_id': 16},
    {'id': 44, 'combo_id': 14, 'subject_id': 3},
    {'id': 45, 'combo_id': 14, 'subject_id': 13},
    {'id': 46, 'combo_id': 15, 'subject_id': 18},
    {'id': 47, 'combo_id': 15, 'subject_id': 17},
    {'id': 48, 'combo_id': 15, 'subject_id': 13}
]

schools = [
    {'id': 1, 'name': 'Green Valley High School', 'fees': 25000, 'location': 'Kolkata'},
    {'id': 2, 'name': 'Riverdale Public School', 'fees': 18000, 'location': 'Chakdaha'},
    {'id': 3, 'name': 'Sunrise International Academy', 'fees': 40000, 'location': 'Delhi'},
    {'id': 4, 'name': 'Harmony Residential School', 'fees': 32000, 'location': 'Bangalore'},
    {'id': 5, 'name': 'Lotus Valley School', 'fees': 27000, 'location': 'Mumbai'},
    {'id': 6, 'name': 'Starlight Convent', 'fees': 22000, 'location': 'Chennai'},
    {'id': 7, 'name': 'Oakridge Global School', 'fees': 55000, 'location': 'Hyderabad'},
    {'id': 8, 'name': 'Silver Oak Academy', 'fees': 30000, 'location': 'Pune'},
    {'id': 9, 'name': 'Bright Future School', 'fees': 20000, 'location': 'Chandigarh'},
    {'id': 10, 'name': 'Wisdom Tree School', 'fees': 24000, 'location': 'Jaipur'}
]

school_subject_combo = [
    {'id': 1, 'school_id': 1, 'combo_id': 1},
    {'id': 2, 'school_id': 1, 'combo_id': 4},
    {'id': 3, 'school_id': 1, 'combo_id': 7},
    {'id': 4, 'school_id': 1, 'combo_id': 12},

    {'id': 5, 'school_id': 2, 'combo_id': 2},
    {'id': 6, 'school_id': 2, 'combo_id': 5},
    {'id': 7, 'school_id': 2, 'combo_id': 8},
    {'id': 8, 'school_id': 2, 'combo_id': 13},

    {'id': 9, 'school_id': 3, 'combo_id': 3},
    {'id': 10, 'school_id': 3, 'combo_id': 6},
    {'id': 11, 'school_id': 3, 'combo_id': 9},
    {'id': 12, 'school_id': 3, 'combo_id': 14},

    {'id': 13, 'school_id': 4, 'combo_id': 1},
    {'id': 14, 'school_id': 4, 'combo_id': 10},
    {'id': 15, 'school_id': 4, 'combo_id': 11},

    {'id': 16, 'school_id': 5, 'combo_id': 2},
    {'id': 17, 'school_id': 5, 'combo_id': 7},
    {'id': 18, 'school_id': 5, 'combo_id': 15},

    {'id': 19, 'school_id': 6, 'combo_id': 3},
    {'id': 20, 'school_id': 6, 'combo_id': 8},
    {'id': 21, 'school_id': 6, 'combo_id': 13},

    {'id': 22, 'school_id': 7, 'combo_id': 4},
    {'id': 23, 'school_id': 7, 'combo_id': 6},
    {'id': 24, 'school_id': 7, 'combo_id': 9},
    {'id': 25, 'school_id': 7, 'combo_id': 14},

    {'id': 26, 'school_id': 8, 'combo_id': 5},
    {'id': 27, 'school_id': 8, 'combo_id': 10},
    {'id': 28, 'school_id': 8, 'combo_id': 12},

    {'id': 29, 'school_id': 9, 'combo_id': 1},
    {'id': 30, 'school_id': 9, 'combo_id': 7},
    {'id': 31, 'school_id': 9, 'combo_id': 11},
    {'id': 32, 'school_id': 9, 'combo_id': 15},

    {'id': 33, 'school_id': 10, 'combo_id': 2},
    {'id': 34, 'school_id': 10, 'combo_id': 3},
    {'id': 35, 'school_id': 10, 'combo_id': 8},
    {'id': 36, 'school_id': 10, 'combo_id': 13}
]

