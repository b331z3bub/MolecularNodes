from .func import (
    button_custom_color,
    button_custom_selection
)

menu_items = {
    'style': [
        {
            'label': 'Presets',
            'name': 'MN_style_presets',
            "description": "Quickly switch between several different pre-made preset styles. Best used when using MolecularNodes via scripts, ensuring all atoms are displayed using a combination of cartoons and atoms.",
            "video_url": "https://imgur.com/gCQRWBk.mp4"
        },
        {
            'label': 'Spheres',
            'name': 'MN_style_spheres',
            "description": "Style to apply the traditional space-filling atomic representation of atoms. Spheres are scaled based on the `vdw_radii` attribute. By default the _Point Cloud_ rendering system is used, which is only visible inside of Cycles.",
            "video_url": "https://imgur.com/KjKkF2u"
        },
        {
            'label': 'Cartoon',
            'name': 'MN_style_cartoon',
            "description": "Style to apply the traditional cartoon representation of protein structures. This style highlights alpha-helices and beta-sheets with arrows and cylinders.",
            "video_url": "https://imgur.com/VGOpMgX"
        },
        {
            'label': 'Ribbon',
            'name': 'MN_style_ribbon',
            "description": "Style that creates a continuous solid ribbon or licorice tube through the backbones of peptides and nucleic acids.",
            "video_url": "https://imgur.com/jGjocfO"
        },
        {
            'label': 'Surface',
            'name': 'MN_style_surface',
            "description": "Style that creates a surface representation based on the proximity of atoms to a probe that is moved through the entire structure.",
            "video_url": "https://imgur.com/nBCb9sg"
        },
        {
            'label': 'Ball and Stick',
            'name': 'MN_style_ball_and_stick',
            "description": "Style that creates cylinders for bonds and spheres for atoms. The atoms can be either Eevee or Cycles compatible, with customisation to resolution and radius possible.",
            "video_url": "https://imgur.com/9KTfcoz"
        },
        {
            'label': 'Stick',
            'name': 'MN_style_stick',
            "description": "Style that creates a cylinder for each bond. Cylindrical caps to the cylinders are currently not supported. Best to use [`MN_style_ball_and_stick`](#style-ball-and-stick).",
            "video_url": "https://imgur.com/4ZK1AMo"
        }
    ],
    'select': [
        {
            'label': 'Separate Atoms',
            'name': 'MN_select_separate_atoms',
            'description': "Select only the desired input atoms. The output is bits of geometry, which include the selection and include the inverse of the selected atoms. You can expand the selection to include an entire residue if a single atom in that residue is selected, by setting `Whole Residue` to `True`.",
            'video_url': "https://imgur.com/VsCW0HY"
        },
        {
            'label': 'Separate Polymers',
            'name': 'MN_select_separate_polymers',
            'description': "Separate the input atomic geometry into it's different polymers or `Protein`, `Nucleic Acid` and `other`.",
            'video_url': 'https://imgur.com/ICQZxxz'
        },
        "break",
        {
            'label': 'custom',
            'function': button_custom_selection,
            'values': [
                {
                    'label': 'Chain',
                    'field': 'chain_id',
                    'name': 'MN_select_chain_',
                    'prefix': 'Chain ',
                    'property_id': 'chain_id_unique',
                    "description": "Select single or multiple of the different chains. Creates a selection based on the `chain_id` attribute.",
                    "video_url": "https://imgur.com/P9ZVT2Z"
                },
                {
                    'label': 'Entity',
                    'field': 'entity_id',
                    'name': 'MN_select_entity_',
                    'prefix': '',
                    'property_id': 'entity_names',
                    "description": "Select single or multiple of the different entities. Creates a selection based on the `entity_id` attribute.",
                    "video_url": "https://imgur.com/fKQIfGZ"
                },
                {
                    'label': 'Ligand',
                    'field': 'res_name',
                    'name': 'MN_select_ligand_',
                    'prefix': '',
                    'property_id': 'ligands',
                    "description": "Select single or multiple of the different ligands.",
                    "video_url": "https://imgur.com/s2seWIw"
                }
            ]
        },
        "break",
        {
            'label': 'Cube',
            'name': 'MN_select_cube',
            "description": "Create a selection that is inside the `Empty_Cube` object. When this node is first created, an _empty_ object called `Empty_Cube` should be created. You can always create additional empty objects through the add menu, to use a different object. The rotation and scale of the object will be taken into account for the selection.",
            "video_url": "https://imgur.com/P4GZ7vq"
        },
        {
            'label': 'Sphere',
            'name': 'MN_select_sphere',
            "description": "Create a selection that is within a spherical radius of an object, based on that object's scale. By default an _empty_ object called `Empty_Sphere` is created. You can use other objects or create a new empty to use. The origin point for the object will be used, which should be taken in to account when using molecules. Use [`MN_select_proximity`](#select-proximity) for selections which are within a certain distance of a selection of atoms instead of a single origin point.",
            "video_url": "https://imgur.com/xdeTZR7"
        },
        "break",
        {
            'label': 'Secondary Structure',
            'name': 'MN_select_sec_struct',
            # or can be calculated using the [`MN_utils_dssp'](#utils-dssp) node.",
            "description": "Select based on the assigned secondary structure information. Only returns a selection if the `sec_struct` attribute exists on the atoms. Will be imported from files where it is present",
            "video_url": "https://imgur.com/IindS3D"
        },
        {
            'label': 'Backbone',
            'name': 'MN_select_backbone',
            "description": "Selection fields for the backbone and side chains of the protein and nucleic acids.",
            "video_url": "https://imgur.com/Sbl6ns5"
        },
        {
            'label': 'Atomic Number',
            'name': 'MN_select_atomic_number',
            'description': "Select single elements, by matching to the `atomic_number` field. Useful for selecting single elements, or combining to select elements higher than 20 on the periodic table.",
            'video_url': "https://imgur.com/Bxn33YK"
        },
        {
            'label': 'Element',
            'name': 'MN_select_element',
            "description": "Select individual elements, for the first 20 elements on the periodic table. For selections of higher elements, use [`MN_select_atomic_number`](#select-atomic-number). Creating a node which includes more elements becomes too large to be practical.",
            "video_url": "https://imgur.com/nRQwamG"
        },
        {
            'label': 'Attribute',
            'name': 'MN_select_attribute',
            "description": "Selections based on the different attributes that are available on the atomic geometry.",
            "video_url": "https://imgur.com/HakZ4sx"
        },
        {
            'label': 'Bonded Atoms',
            'name': 'MN_select_bonded',
            "description": "Based on an initial selection, finds atoms which are within a certain number of bonds of this selection. Output can include or excluded the original selection.",
            "video_url": "https://imgur.com/g8hgXup"
        },
        "break",
        {
            'label': 'Res ID',
            'name': 'mn.residues_selection_custom',
            'backup': 'MN_select_res_id_',
            "description": "Create a more complex selection for the `res_id` field, by specifying multiple ranges and potential single `res_id` numbers. This node is built uniquely each time, to the inputs will look different for each user.\nIn the example below, residues 10 & 15 are selected, as well as residues between and including 20-100.\nThe node was created by inputting `10, 15, 20-100` into the node creation field.",
            "video_url": "https://imgur.com/OwAXsbG"
        },
        {
            'label': 'Proximity',
            'name': 'MN_select_proximity',
            "description": "Create a selection based on the proximity to the Target Atoms of the input. A sub-selection of the Target atoms can be used if the `Selection` input is used. You can expand the selection to include an entire residue if a single atom in that residue is selected, by setting `Whole Residue` to `True`.\nIn the example below, the `MN_style_atoms` is being applied to a selection, which is being calculated from the proximity of atoms to specific chains. As the cutoff for the selection is changed, it includes or excludes more atoms. The `Whole Residue` option also ensures that entire residues are shown.",
            "video_url": "https://imgur.com/RI80CRY"
        },
        {
            'label': 'Res ID Single',
            'name': 'MN_select_res_id_single',
            "description": "Select a single residue based on the `res_id` number.",
            "video_url": "https://imgur.com/BL6AOP4"
        },
        {
            'label': 'Res ID Range',
            'name': 'MN_select_res_id_range',
            "description": "Select multiple residues by specifying a _minimum_ and a _maximum_ which will create the selection based on the `res_id` number.",
            "video_url": "https://imgur.com/NdoQcdE"
        },
        {
            'label': 'Res Name Peptide',
            'name': 'MN_select_res_name_peptide',
            "description": "Select single or multiple protein residues by name. Includes the 20 naturally occurring amino acids.",
            "video_url": "https://imgur.com/kjzH9Rs"
        },
        {
            'label': 'Res Name Nucleic',
            'name': 'MN_select_res_name_nucleic',
            "description": "Select single or multiple nucleic residues by name.",
            "video_url": "https://imgur.com/qnUlHpG"
        },
        {
            'label': 'Res Whole',
            'name': 'MN_select_res_whole',
            "description": "Expand the given selection to include a whole residue, if a single atom in that residue is selected. Useful for when a distance or proximity selection includes some of the residue and you wish to include all of the residue.",
            "video_url": "https://imgur.com/JFzwE0i"
        },
    ],
    'color': [
        {
            'label': 'Set Color',
            'name': 'MN_color_set',
            "description": "The is the primary way to change the color of structures in Molecular Nodes. Colors for cartoon and ribbon are taken from the _alpha-carbons_ of the structures. Change the color of the input atoms, based on a selection and a color field. The color field can be as complex of a calculation as you wish. In the example below the color for the whole structure can be set, or the color can be based on a color for each chain, or the result of mapping a color to an attribute such as `b_factor`.",
            "video_url": "https://imgur.com/667jf0O"
        },
        "break",
        {
            'label': 'custom',
            'function': button_custom_color,
            'values': [
                {
                    'label': 'Chain',
                    'field': 'chain_id',
                    'name': 'MN_select_chain_',
                    'prefix': 'Chain',
                    'property_id': 'chain_id_unique',
                    "description": "Choose the colors for individual chains in the structure. This node is generated for each particular molecule, so the inputs will look different based on the imported structure. For larger structures with many chains this node may become too large to be practical, in which case you might better use [`MN_color_entity_id`](#color-entity-id).",
                    "video_url": "https://imgur.com/9oM24vB"
                },
                {
                    'label': 'Entity',
                    'field': 'entity_id',
                    'name': 'MN_color_entity_',
                    'prefix': '',
                    'property_id': 'entity_names',
                    "description": "Choose the colors for individual entities in the structure. Multiple chains may be classified as the same entity, if they are copies of the same chain but in different conformations or positions and rotations. The nodes is generated for each individual structure, if `entity_id` is available.",
                    "video_url": "https://imgur.com/kEvj5Jk"
                },
                {
                    'label': 'Ligand',
                    'field': 'res_name',
                    'name': 'MN_color_ligand_',
                    'prefix': '',
                    'property_id': 'ligands',
                    "description": "Choose the colors for individual ligands in the structure.",
                    "video_url": "https://imgur.com/bQh8Fd9"
                }
            ]
        },
        "break",
        {
            'label': 'Goodsell Colors',
            'name': 'MN_color_goodsell',
            "description": "Change the inputted color to be darker for non-carbon atoms. Creates a _Goodsell Style_ color scheme for individual chains.",
            "video_url": "https://imgur.com/gPgMSRa"
        },
        {
            'label': 'Attribute Map',
            'name': 'MN_color_attribute_map',
            "description": "Interpolate between two or three colors, based on the value of an attribute field such as `b_factor`. Choosing the minimum and maximum values with the inputs.",
            "video_url": "https://imgur.com/lc2o6e1"
        },
        {
            'label': 'Attribute Random',
            'name': 'MN_color_attribute_random',
            "description": "Generate a random color, based on the given attribute. Control the lightness and saturation of the color with the inputs.",
            "video_url": "https://imgur.com/5sMcpAu"
        },
        {
            'label': 'Backbone',
            'name': 'MN_color_backbone',
            'description': ""
        },
        {
            'label': 'pLDTT',
            'name': 'MN_color_pLDTT',
            'description': 'Assigns colors using the `b_factor` attribute, which contains the `pLDTT` attribute for models that come from AlphaFold.'
        },
        {
            'label': 'Secondary Structure',
            'name': 'MN_color_sec_struct',
            "description": "Choose a color for the different secondary structures, based on the `sec_struct` attribute.",
            "video_url": "https://imgur.com/wcJAUp9"
        },
        "break",
        {
            'label': 'Element',
            'name': 'MN_color_element',
            "description": "Choose a color for each of the first 20 elements on the periodic table. For higher atomic number elements use [`MN_color_atomic_number`](#color-atomic-number).",
            "video_url": "https://imgur.com/iMGZKCx"
        },
        {
            'label': 'Atomic Number',
            'name': 'MN_color_atomic_number',
            "description": "Choose a color for an individual element. Select the element based on `atomic_number`. Useful for higher atomic number elements which are less commonly found in structures.",
            "video_url": "https://imgur.com/pAloaAF"
        },
        {
            'label': 'Res Name Peptide',
            'name': 'MN_color_res_name_peptide',
            "description": "Choose a color for each of the 20 naturally occurring amino acids. Non AA atoms will retain their currently set color.",
            "video_url": "https://imgur.com/1yhSVsW"
        },
        {
            'label': 'Res Name Nucleic',
            'name': 'MN_color_res_name_nucleic',
            "description": "Choose a color for each of the nucleic acids. Non nucleic acid atoms will retain their currently set color.",
            "video_url": "https://imgur.com/LpLZT3F"
        },

        {
            'label': 'Element Common',
            'name': 'MN_color_common',
            "description": "Choose a color for each of the common elements. This is a smaller convenience node for elements which commonly appear in macromolecular structures. Use [`MN_color_element`](#color-element) for the first 20 elements and [`MN_color_atomic_number`](#color-atomic-number) for individual elements with higher atomic numbers.",
            "video_url": "https://imgur.com/GhLdNwy"
        },
    ],

    'topology': [
        {
            'label': 'Edge Info',
            'name': 'MN_topo_edge_info',
            'description': 'Get information for the selected edge, evaluated on the point domain. The "Edge Index" selects the edge from all possible connected edges. Edges are unfortunately stored somewhat randomly. The resulting information is between the evaluating point and the point that the edge is between. Point Index returns -1 if not connected.\n\nIn the video example, cones are instanced on each point where the Edge Index returns a valid connection. The Edge Vector can be used to align the instanced cone along that edge. The length of the edge can be used to scale the cone to the other point. As the "Edge Index" is changed, the selected edge changes. When "Edge Index" == 3, only the atoms with 4 connections are selected, which in this model (1BNA) are just the phosphates.',
            'video_url': "https://imgur.com/Ykyis3e"
        },
        {
            'label': 'Edge Angle',
            'name': 'MN_topo_edge_angle',
            'description': ' Calculate the angle between two edges, selected with the edge indices. For molecule bonds, combinations of [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)] will select all possible bond angles.\n\nIn the video example, two edges are selected with their "Edge Index" values. Those atoms which aren\'t valid return false and do not get instanced. The two edge vectors are used to calculate the perpendicular vector through cross product, around which the rotation for the cone is rotated. This demonstrates the ability to calculate the edge angle between the two selected edges.',
            "video_url": "https://imgur.com/oQP6Cv8"
        },
        {
            'label': 'Connected Points for Edge Point',
            'name': 'MN_topo_edge_connected_points',
            'description': 'Finds the conntected point for the selected "Edge Index", and returns each point index for all of the points connected to that point. If the connection doesn\'t exist, or the connection is back to the original point, -1 is returned.\n\nIn the video example, a new point is selected based on the "Edge Index". At that point, all of the connecting points are exposed as indices `0, 1, 2, 3`. If that index is not a valid point or connection, or the point is the same as the original point that is being evaluated, then -1 is returned. \n\nThis is one of the more complicated topology nodes, but allows indexing of the atoms that are bonded to a bonded atom. This helps with doing calculations for planar molecules.',
            'video_url': 'https://imgur.com/fZ6srIS',
        },
        "break",
        {
            'label': 'Backbone Positions',
            'name': 'MN_topo_backbone',
            'description': 'If the atoms have been through the "Compute Backbone" node, then the backbone atom positions will be available as attributes through this node.\n\nIn the video example, the `Alpha Carbons` output is styled as spheres, where the position is mixed with some of the backbone posiitons. The backbone positions can also be selected from the AA residue higher or lower with the specified offset.',
            'video_url': 'https://imgur.com/6X2wnpY'
        },
        {
            'label': 'Compute Backbone',
            'name': 'MN_topo_compute_backbone',
            'description': 'Gets the backbone positions for each AA residue and stores them as attributes, and additionally computes the phi and psi angles for each residue in radians.\n\nIn the video example, the Phi and Psi angles are mapped from (-Pi, Pi) to (0, 1), which is used in the Color Ramp node to choose colors. This is computed on the alpha carbons, but can be used on any of the resulting atoms for the corresponding residues, which is shown in the second video.',
            'video_url': ['https://imgur.com/9DNzngY', 'https://imgur.com/W3P9l10']
        },
        "break",
        {
            'label': '3-Point Angle',
            'name': 'MN_topo_angle_3point',
            'description': 'Calculate the angle between 3 different points. These points are selected based on their index in the point domain, with Index B being the centre of the calculation.\n\nIn the video example, the same calculation that is occurring internally inside of the `MN_topo_edge_angle` node, is being handled explicity by this node. If the `Index` is being used as `Index B` then the current point that is being evaluated is the centre of the angle calculation. If this value is changed, then the point at the corresponding index is used, which results in a smaller angle in the example video.',
            'video_url': 'https://imgur.com/qXyy2ln'
        },
        {
            'label': '2-Point Angle',
            'name': 'MN_topo_angle_2point',
            'description': 'Calculate the angle that two points make, relative to the current point being evaluated. Points are selected based on their index, with the centre of the angle calculation being the current point\'s position. Equivalent to using 3-Point angle and using `Index` as the `Index B`.\n\nIn the example video, the angle calculation is similar to that of the 3-Point Angle node, but the middle point is always the current point.',
            'video_url': 'https://imgur.com/xp7Vbaj'
        },
        {
            'label': 'Point Distance',
            'name': 'MN_topo_point_distance',
            'description': 'Calculate the distance and the vector between the evaluating point and the point selected via the Index.\n\nIn the example video, each point is calculating a vector and a distance between itself and the indexed point. When the Point Mask node is used, this index is then on a per-group basis, so each point in the group points to just the group\'s corresponding point.',
            'video_url': 'https://imgur.com/AykNvDz'
        },
        "break",
        {
            'label': 'Group Point Mask',
            'name': 'MN_topo_point_mask',
            'description': 'Returns the index for the atom for each unique group (from res_id) for each point in that group. Allows for example, all atoms in a group to be rotated around the position of the selected atom.\n\nIn the video example, the `atom_name` is used to select an atom within the groups. Each atom\'s position is then offset to that position, showing the group-wise selection.',
            'video_url': 'https://imgur.com/sD3jRTR'
        },
    ],

    'bonds': [
        {
            'label': 'Find Bonds',
            'name': '.MN_bonds_find',
            'description': "Finds bonds between atoms based on distance. Based on the vdw_radii for each point, finds other points within a certain radius to create a bond to. Does not preserve the index for the points. Does not detect bond type"
        },
        {
            'label': 'Break Bonds',
            'name': '.MN_bonds_break',
            'description': "Will delete a bond between atoms that already exists based on a distance cutoff"
        }
    ],

    'assembly': [
        {
            'label': 'Biological Assembly',
            'name': 'mn.assembly_bio',
            'backup': 'MN_assembly_',
            "description": "Creates a biological assembly by applying rotation and translation matrices to individual chains in the structure. It is created on an individual molecule basis, if assembly instructions are detected when imported.",
            "video_url": "https://imgur.com/6jyAP1z"
        },
        {
            'label': 'Center Assembly',
            'name': 'MN_assembly_center',
            "description": "Move an instanced assembly to the world origin. Some structures are not centred on the world origin, so this node can reset them to the world origin for convenient rotation and translation and animation.",
            "video_url": "https://imgur.com/pgFTmgC"
        }
    ],


    'DNA': [
        {
            'label': 'Double Helix',
            'name': 'MN_dna_double_helix',
            'description': "Create a DNA double helix from an input curve.\nTakes an input curve and instances for the bases, returns instances of the bases in a double helix formation"
        },
        {
            'label': 'Bases',
            'name': 'MN_dna_bases',
            'description': "Provide the DNA bases as instances to be styled and passed onto the Double Helix node"
        },
        "break",
        {
            'label': 'Style Spheres Cycles',
            'name': 'MN_dna_style_spheres_cycles',
            'description': "Style the DNA bases with spheres only visible in Cycles"
        },
        {
            'label': 'Style Spheres EEVEE',
            'name': 'MN_dna_style_spheres_eevee',
            'description': "Style the DNA bases with spheres visible in Cycles and EEVEE"
        },
        {
            'label': 'Style Surface',
            'name': 'MN_dna_style_surface',
            'description': "Style the DNA bases with surface representation"
        },
        {
            'label': 'Style Ball and Stick',
            'name': 'MN_dna_style_ball_and_stick',
            'description': "Style the DNA bases with ball and stick representation"
        }
    ],

    'animate': [
        {
            'label': 'Animate Frames',
            'name': 'MN_animate_frames',
            "description": "Animate the atoms of a structure, based on the frames of a trajectory from the `Frames` collection in the input. The structure animates through the trajectory from the given start frame to the given end frame, as the `Animate 0..1` value moves from `0` to `1`. Values higher than `1` start at the beginning again and the trajectory will loop repeating every `1.00`.\nPosition and `b_factor` are interpolated if available. By default linear interpolation is used. Smoothing in and out of each frame can be applied with the `Smoother Step`, or no interpolation at all.",
            "video_url": "https://imgur.com/m3BPUxh"
        },
        {
            'label': 'Animate Value',
            'name': 'MN_animate_value',
            "description": "Animate a float value between the specified min and max values, over specified range of frames. If clamped, frames above and below the start and end will result in the min and max output values, otherwise it will continue to linearly interpolate the value beyond the min and max values.",
            "video_url": "https://imgur.com/2oOnwRm"
        },
        "break",
        {
            'label': 'Res Wiggle',
            'name': 'MN_animate_res_wiggle',
            "description": "Create a procedural animation of side-chain movement. 'Wiggles' the side-chains of peptide amino acids based on the `b_factor` attribute. Wiggle is currently only supported for protein side-chains and does not check for steric clashing so higher amplitudes will result in strange results. The animation should seamlessly loop every `1.00` of the `Animate 0..1` input.",
            "video_url": "https://imgur.com/GK1nyUz"
        },
        {
            'label': 'Res to Curve',
            'name': 'MN_animate_res_to_curve',
            "description": "Take the protein residues from a structure and align then along an input curve. Editing the curve will change how the atoms are arranged. The output atoms can be styled as normal.",
            "video_url": "https://imgur.com/FcEXSZx"
        },
        "break",
        {
            'label': 'Noise Position',
            'name': 'MN_animate_noise_position',
            "description": "Create 3D noise vector based on the position of points in 3D space. Evolve the noise function with the `Animate` input, and change the characteristics of the noise function with the other inputs such as scale and detail. There is also a 1-dimensional noise output called `Fac`.\n\nAn example of using this noise is to offset the positions of atoms with the `Set Position` node.",
            "video_url": "https://imgur.com/B8frW1C"
        },
        {
            'label': 'Noise Field',
            'name': 'MN_animate_noise_field',
            "description": "Create a 3D noise vector based on the input field. Evolve the noise function with the `Animate` input, and change the characteristics of the noise function with the other inputs such as scale and detail. There is also a 1-dimensional noise output called `Fac`.\n\nAn example of using this noise is to offset the positions of atoms with the `Set Position` node. Different field inputs result in different noise being applied. Using the `chain_id` results in the same noise being generated for each atom in each chain, but different between chains.",
            "video_url": "https://imgur.com/hqemVQy"
        },
        {
            'label': 'Noise Repeat',
            'name': 'MN_animate_noise_repeat',
            "description": "Create a 3D noise vector based on the input field, that repeats every `1.00` for the `Animate 0..1` input. Evolve the noise function with the `Animate` input, and change the characteristics of the noise function with the other inputs such as scale and detail. There is also a 1-dimensional noise output called `Fac`.\n\nAn example of using this noise is to offset the positions of atoms with the `Set Position` node. Different field inputs result in different noise being applied. Using the `chain_id` results in the same noise being generated for each atom in each chain, but different between chains.",
            "video_url": "https://imgur.com/GNQcIlx"
        }
    ],

    'utils': [
        {
            'label': 'Curve Resample',
            'name': 'MN_utils_curve_resample',
            'description': ''
        },
        {
            'label': 'Vector Angle',
            'name': 'MN_utils_vector_angle',
            'description': 'Compute the angle in radians between two vectors.'
        },
        {
            'label': 'Vector Axis Angle',
            'name': 'MN_utils_vector_angle_axis',
            'description': 'Computes the angle between two vectors, AB & CD around around the axis of BC. The first vector AB is treated as the "12 O\'clock" up position, looking down the axis towards C, with angles being return in the range of (-Pi, Pi). Clockwise angles are positive and anti-clockwise angles are negative.',
            'video_url': ''
        },
        # {
        #     'label': 'Determine Secondary Structure',
        #     'name': 'MN_utils_dssp',
        #     'description': ''
        #     },
        {
            'label': 'Cartoon Utilities',
            'name': '.MN_utils_style_cartoon',
            'description': 'The underlying node group which powers the cartoon style'
        },
        {
            'label': 'Spheres Cycles',
            'name': '.MN_utils_style_spheres_cycles',
            'description': 'A sphere atom representation, visible ONLY in Cycles. Based on point-cloud rendering'
        },
        {
            'label': 'Spheres EEVEE',
            'name': '.MN_utils_style_spheres_eevee',
            'description': 'A sphere atom representation, visible in EEVEE and Cycles. Based on mesh instancing which slows down viewport performance'
        }
    ],

    'cellpack': [
        {
            'label': 'Pack Instances',
            'name': 'MN_pack_instances',
            'description': ''
        }
    ],

    'density': [
        {
            'label': 'Style Surface',
            'name': 'MN_density_style_surface',
            "description": "A surface made from the electron density given a certain threshold value.",
            "video_url": "https://imgur.com/jGgMSd4"
        },
        {
            'label': 'Style Wire',
            'name': 'MN_density_style_wire',
            "description": "A wire surface made from the electron density given a certain threshold value.",
            "video_url": "https://imgur.com/jGgMSd4"
        },
        {
            'label': 'Sample Nearest Attribute',
            'name': 'MN_density_sample_nearest',
            "description": "Sample the nearest atoms from another object, to get the colors or other attributes and apply them to a volume mesh.",
            "video_url": "https://imgur.com/UzNwLv2"
        }
    ]
}
