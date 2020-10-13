import open3d

## POINT CLOUD -> POINT CLOUD
# ptcd = open3d.io.read_point_cloud("fragment.pcd")
# # open3d.io.write_point_cloud("fragment.ply", ptcd)
# open3d.io.write_point_cloud("fragment2.xyz", ptcd)

## MESH -> MESH
mesh = open3d.io.read_triangle_mesh("knot.ply")
open3d.io.write_triangle_mesh("knot_mesh.ply", mesh)

## MESH -> POINT CLOUD
# ptcd = open3d.io.read_point_cloud("knot.ply")
# open3d.io.write_point_cloud("knot_pcd.ply", ptcd)