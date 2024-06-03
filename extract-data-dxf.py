import ezdxf

def extract_dwg_data(file_path):
    try:
        # Leer el archivo DXF
        doc = ezdxf.readfile(file_path)
    except IOError:
        print(f"No se puede leer el archivo: {file_path}")
        return None
    except ezdxf.DXFStructureError:
        print(f"Archivo DXF no válido: {file_path}")
        return None

    # Obtener el espacio de modelo
    modelspace = doc.modelspace()

    def extract_entities(entities):
        extracted_data = []
        for entity in entities:
            entity_data = {"type": entity.dxftype()}
            if entity.dxftype() == 'LINE':
                entity_data["start_point"] = entity.dxf.start
                entity_data["end_point"] = entity.dxf.end
            elif entity.dxftype() == 'CIRCLE':
                entity_data["center_point"] = entity.dxf.center
                entity_data["radius"] = entity.dxf.radius
            elif entity.dxftype() == 'ARC':
                entity_data["center_point"] = entity.dxf.center
                entity_data["radius"] = entity.dxf.radius
                entity_data["start_angle"] = entity.dxf.start_angle
                entity_data["end_angle"] = entity.dxf.end_angle
            elif entity.dxftype() == 'LWPOLYLINE':
                entity_data["points"] = entity.get_points()
            elif entity.dxftype() == 'POLYLINE':
                entity_data["points"] = [v.dxf.location for v in entity.vertices]
            elif entity.dxftype() == 'ELLIPSE':
                entity_data["center_point"] = entity.dxf.center
                entity_data["major_axis"] = entity.dxf.major_axis
                entity_data["ratio"] = entity.dxf.ratio
                entity_data["start_param"] = entity.dxf.start_param
                entity_data["end_param"] = entity.dxf.end_param
            elif entity.dxftype() == 'TEXT':
                entity_data["text"] = entity.dxf.text
                entity_data["insert_point"] = entity.dxf.insert
            elif entity.dxftype() == 'MTEXT':
                entity_data["text"] = entity.text
                entity_data["insert_point"] = entity.dxf.insert
            elif entity.dxftype() == 'HATCH':
                entity_data["pattern_name"] = entity.dxf.pattern_name
                entity_data["solid_fill"] = entity.dxf.solid_fill
                entity_data["associative"] = entity.dxf.associative
                entity_data["paths"] = [path.vertices for path in entity.paths]
            elif entity.dxftype() == 'SOLID':
                entity_data["points"] = entity.get_points()
            elif entity.dxftype() == 'POINT':
                entity_data["location"] = entity.dxf.location
            elif entity.dxftype() == 'DIMENSION':
                entity_data = extract_dimension_data(entity)
            elif entity.dxftype() == 'INSERT':
                block_data = extract_entities(doc.blocks[entity.dxf.name])
                entity_data["block_name"] = entity.dxf.name
                entity_data["block_data"] = block_data
            elif entity.dxftype() == 'LEADER':
                entity_data["vertices"] = entity.vertices
                entity_data["has_arrowhead"] = entity.dxf.has_arrowhead
            elif entity.dxftype() == 'MLINE':
                entity_data["vertices"] = entity.vertices
                entity_data["style"] = entity.dxf.style_name
            elif entity.dxftype() == 'SPLINE':
                entity_data["degree"] = entity.dxf.degree
                entity_data["fit_points"] = entity.fit_points
                entity_data["control_points"] = entity.control_points
            elif entity.dxftype() == '3DFACE':
                entity_data["points"] = entity.get_points()
            elif entity.dxftype() == 'IMAGE':
                entity_data["image_def"] = entity.dxf.image_def
                entity_data["insert_point"] = entity.dxf.insert
                entity_data["u_vector"] = entity.dxf.u_vector
                entity_data["v_vector"] = entity.dxf.v_vector
                entity_data["size"] = entity.dxf.image_size
                entity_data["clipping_boundary"] = entity.clip_boundary
            elif entity.dxftype() == 'UNDERLAY':
                entity_data["underlay_def"] = entity.dxf.underlay_def
                entity_data["insert_point"] = entity.dxf.insert
                entity_data["scale_x"] = entity.dxf.scale_x
                entity_data["scale_y"] = entity.dxf.scale_y
                entity_data["scale_z"] = entity.dxf.scale_z
                entity_data["rotation"] = entity.dxf.rotation
                entity_data["clip_boundary"] = entity.clip_boundary
            elif entity.dxftype() == 'WIPEOUT':
                entity_data["points"] = entity.get_points()
                entity_data["image_def"] = entity.dxf.image_def
            elif entity.dxftype() == 'XLINE':
                entity_data["start_point"] = entity.dxf.start
                entity_data["unit_direction"] = entity.dxf.unit_direction
            elif entity.dxftype() == 'RAY':
                entity_data["start_point"] = entity.dxf.start
                entity_data["unit_direction"] = entity.dxf.unit_direction
            elif entity.dxftype() == 'HELIX':
                entity_data["base_point"] = entity.dxf.base_point
                entity_data["top_point"] = entity.dxf.top_point
                entity_data["radius"] = entity.dxf.radius
                entity_data["turns"] = entity.dxf.turns
            elif entity.dxftype() == 'LIGHT':
                entity_data["light_type"] = entity.dxf.light_type
                entity_data["position"] = entity.dxf.position
                entity_data["target"] = entity.dxf.target
                entity_data["color"] = entity.dxf.color
                entity_data["intensity"] = entity.dxf.intensity
                entity_data["status"] = entity.dxf.status
            elif entity.dxftype() == 'SECTION':
                entity_data["name"] = entity.dxf.name
                entity_data["flags"] = entity.dxf.flags
                entity_data["entities"] = extract_entities(entity)
            elif entity.dxftype() == 'MLEADER':
                entity_data["content"] = entity.dxf.content
                entity_data["style"] = entity.dxf.style
                entity_data["leader_line_positions"] = entity.dxf.leader_line_positions
                entity_data["leader_direction"] = entity.dxf.leader_direction
            elif entity.dxftype() == 'TOLERANCE':
                entity_data["insert_point"] = entity.dxf.insert
                entity_data["x_axis"] = entity.dxf.x_axis
                entity_data["y_axis"] = entity.dxf.y_axis
                entity_data["height"] = entity.dxf.height
                entity_data["content"] = entity.dxf.content
            elif entity.dxftype() == 'MESH':
                entity_data["vertices"] = entity.vertices
                entity_data["faces"] = entity.faces
            elif entity.dxftype() == 'SURFACE':
                entity_data["control_points"] = entity.control_points
                entity_data["knots_u"] = entity.knots_u
                entity_data["knots_v"] = entity.knots_v
                entity_data["degree_u"] = entity.dxf.degree_u
                entity_data["degree_v"] = entity.dxf.degree_v
            elif entity.dxftype() == 'CONTOUR':
                entity_data["vertices"] = entity.vertices
                entity_data["flags"] = entity.dxf.flags
            elif entity.dxftype() == 'VIEWPORT':
                entity_data["view_center_point"] = entity.dxf.view_center_point
                entity_data["snap_base_point"] = entity.dxf.snap_base_point
                entity_data["view_height"] = entity.dxf.view_height
                entity_data["view_aspect_ratio"] = entity.dxf.view_aspect_ratio
            else:
                entity_data["data"] = str(entity)  # para entidades no reconocidas

            extracted_data.append(entity_data)
        return extracted_data

    def extract_dimension_data(entity):
        dim_data = {
            "dimtype": entity.dimtype,
            "text": entity.dxf.text,
            "insert_point": entity.dxf.insert,
        }
        dim_type = entity.dimtype

        if dim_type == 0:  # Rotated, horizontal, or vertical linear dimension
            dim_data["defpoints"] = [entity.dxf.defpoint, entity.dxf.defpoint2]
        elif dim_type == 1:  # Aligned linear dimension
            dim_data["defpoints"] = [entity.dxf.defpoint, entity.dxf.defpoint2]
        elif dim_type == 2:  # Angular dimension (2 lines)
            dim_data["defpoints"] = [entity.dxf.defpoint, entity.dxf.defpoint2, entity.dxf.defpoint3, entity.dxf.defpoint4]
        elif dim_type == 3:  # Diameter dimension
            dim_data["defpoints"] = [entity.dxf.defpoint, entity.dxf.defpoint2]
        elif dim_type == 4:  # Radius dimension
            dim_data["defpoints"] = [entity.dxf.defpoint, entity.dxf.defpoint2]
        elif dim_type == 5:  # Angular dimension (3 points)
            dim_data["defpoints"] = [entity.dxf.defpoint, entity.dxf.defpoint2, entity.dxf.defpoint3]
        elif dim_type == 6:  # Angular dimension (4 points)
            dim_data["defpoints"] = [entity.dxf.defpoint, entity.dxf.defpoint2, entity.dxf.defpoint3, entity.dxf.defpoint4]
        return dim_data

    data = extract_entities(modelspace)

    return data

def create_dwg_file(output_path, data):
    doc = ezdxf.new(dxfversion="R2010")
    modelspace = doc.modelspace()

    for entity in data:
        entity_type = entity.get("type")
        if entity_type == "LINE":
            modelspace.add_line(entity["start_point"], entity["end_point"])
        elif entity_type == "CIRCLE":
            modelspace.add_circle(entity["center_point"], entity["radius"])
        elif entity_type == "ARC":
            modelspace.add_arc(entity["center_point"], entity["radius"], entity["start_angle"], entity["end_angle"])
        elif entity_type == "LWPOLYLINE":
            modelspace.add_lwpolyline(entity["points"])
        elif entity_type == "POLYLINE":
            polyline = modelspace.add_polyline3d()
            for point in entity["points"]:
                polyline.append_vertices(point)
        elif entity_type == "ELLIPSE":
            modelspace.add_ellipse(entity["center_point"], entity["major_axis"], entity["ratio"], entity["start_param"], entity["end_param"])
        elif entity_type == "TEXT":
            modelspace.add_text(entity["text"], dxfattribs={'insert': entity["insert_point"]})
        elif entity_type == "MTEXT":
            modelspace.add_mtext(entity["text"], dxfattribs={'insert': entity["insert_point"]})
        elif entity_type == "HATCH":
            hatch = modelspace.add_hatch()
            hatch.set_pattern_fill(entity["pattern_name"], scale=1)
            hatch.paths.add_polyline_path(entity["paths"], is_closed=True)
        elif entity_type == "SOLID":
            modelspace.add_solid(entity["points"])
        elif entity_type == "POINT":
            modelspace.add_point(entity["location"])
        elif entity_type == "DIMENSION":
            dim_data = entity
            dim_type = dim_data["dimtype"]
            if dim_type == 0:  # Linear dimension
                modelspace.add_linear_dim(base=dim_data["defpoints"][0], p1=dim_data["defpoints"][1], text=dim_data["text"])
            elif dim_type == 1:  # Aligned dimension
                modelspace.add_aligned_dim(base=dim_data["defpoints"][0], p1=dim_data["defpoints"][1], text=dim_data["text"])
            elif dim_type == 2:  # Angular dimension (2 lines)
                modelspace.add_angular_dim(base=dim_data["defpoints"][0], p1=dim_data["defpoints"][1], text=dim_data["text"])
            elif dim_type == 3:  # Diameter dimension
                modelspace.add_diameter_dim(center=dim_data["defpoints"][0], p1=dim_data["defpoints"][1], text=dim_data["text"])
            elif dim_type == 4:  # Radius dimension
                modelspace.add_radius_dim(center=dim_data["defpoints"][0], p1=dim_data["defpoints"][1], text=dim_data["text"])
            elif dim_type == 5:  # Angular dimension (3 points)
                modelspace.add_angular_dim(base=dim_data["defpoints"][0], p1=dim_data["defpoints"][1], text=dim_data["text"])
            elif dim_type == 6:  # Angular dimension (4 points)
                modelspace.add_angular_dim(base=dim_data["defpoints"][0], p1=dim_data["defpoints"][1], text=dim_data["text"])
        elif entity_type == "INSERT":
            modelspace.add_blockref(entity["block_name"], insert=entity["block_data"][0].get("insert_point", (0,0,0)))
        elif entity_type == "LEADER":
            modelspace.add_leader(entity["vertices"], dxfattribs={'has_arrowhead': entity["has_arrowhead"]})
        elif entity_type == "MLINE":
            modelspace.add_mline(entity["vertices"], dxfattribs={'style': entity["style"]})
        elif entity_type == "SPLINE":
            modelspace.add_spline(fit_points=entity["fit_points"], degree=entity["degree"], dxfattribs={'control_points': entity["control_points"]})
        elif entity_type == "3DFACE":
            modelspace.add_3dface(entity["points"])
        elif entity_type == "IMAGE":
            modelspace.add_image(entity["image_def"], insert=entity["insert_point"], size=entity["size"], u_vector=entity["u_vector"], v_vector=entity["v_vector"], dxfattribs={'clipping_boundary': entity["clipping_boundary"]})
        elif entity_type == "UNDERLAY":
            modelspace.add_underlay(entity["underlay_def"], insert=entity["insert_point"], scale=(entity["scale_x"], entity["scale_y"], entity["scale_z"]), rotation=entity["rotation"], dxfattribs={'clip_boundary': entity["clip_boundary"]})
        elif entity_type == "WIPEOUT":
            modelspace.add_wipeout(entity["points"], dxfattribs={'image_def': entity["image_def"]})
        elif entity_type == "XLINE":
            modelspace.add_xline(entity["start_point"], entity["unit_direction"])
        elif entity_type == "RAY":
            modelspace.add_ray(entity["start_point"], entity["unit_direction"])
        elif entity_type == "HELIX":
            modelspace.add_helix(entity["base_point"], entity["top_point"], entity["radius"], entity["turns"])
        elif entity_type == "LIGHT":
            modelspace.add_light(entity["light_type"], entity["position"], target=entity["target"], dxfattribs={'color': entity["color"], 'intensity': entity["intensity"], 'status': entity["status"]})
        elif entity_type == "SECTION":
            section = modelspace.add_section(entity["name"], dxfattribs={'flags': entity["flags"]})
            section_entities = entity["entities"]
            for section_entity in section_entities:
                section.add_entity(section_entity)
        elif entity_type == "MLEADER":
            modelspace.add_mleader(entity["content"], dxfattribs={'style': entity["style"], 'leader_line_positions': entity["leader_line_positions"], 'leader_direction': entity["leader_direction"]})
        elif entity_type == "TOLERANCE":
            modelspace.add_tolerance(entity["content"], dxfattribs={'insert': entity["insert_point"], 'x_axis': entity["x_axis"], 'y_axis': entity["y_axis"], 'height': entity["height"]})
        elif entity_type == "MESH":
            mesh = modelspace.add_mesh()
            mesh.vertices = entity["vertices"]
            mesh.faces = entity["faces"]
        elif entity_type == "SURFACE":
            modelspace.add_surface(entity["control_points"], degree=(entity["degree_u"], entity["degree_v"]), dxfattribs={'knots_u': entity["knots_u"], 'knots_v': entity["knots_v"]})
        elif entity_type == "CONTOUR":
            modelspace.add_contour(entity["vertices"], dxfattribs={'flags': entity["flags"]})
        elif entity_type == "VIEWPORT":
            modelspace.add_viewport(entity["view_center_point"], view_height=entity["view_height"], dxfattribs={'snap_base_point': entity["snap_base_point"], 'view_aspect_ratio': entity["view_aspect_ratio"]})
        # Agregar lógica para otros tipos de entidades según sea necesario

    doc.saveas(output_path)

# Uso del script
dwg_file = r"C:\\Users\\xhito\\Desktop\\DATA SCIENCE\\eDocument\\data\\Weld-Neck-Flange-2-Inch-Class-300.dxf"
output_file = r"C:\\Users\\xhito\\Desktop\\DATA SCIENCE\\eDocument\\data\\extracted_data.dxf"
extracted_data = extract_dwg_data(dwg_file)

# Guardar los datos extraídos en un nuevo archivo DXF
if extracted_data:
    create_dwg_file(output_file, extracted_data)

# Ejemplo de cómo usar los datos extraídos
if extracted_data:
    output = ",\n".join(str(entity) for entity in extracted_data)
    print(output)
