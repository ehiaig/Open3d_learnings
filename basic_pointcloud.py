import open3d

ptcd = open3d.io.read_point_cloud("fragment.ply")
open3d.visualization.draw_geometries([ptcd])