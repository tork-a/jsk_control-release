# camera_view.py
import math
import numpy
import tf
import rospy
import imp
try:
  imp.find_module("view_controller_msgs")
except:
  import roslib; roslib.load_manifest('jsk_teleop_joy')

from view_controller_msgs.msg import CameraPlacement

class CameraView():
  def __init__(self):
    self.yaw = 0.0
    self.pitch = 0.0
    #self.roll = 0.0
    self.distance = 2.0
    self.focus = numpy.array((0, 0, 0))
    self.z_up = numpy.array((0, 0, 1))

  @staticmethod
  def createFromCameraPlacement(camera_placement):
    instance = CameraView()
    ceye = numpy.array((camera_placement.eye.point.x,
                        camera_placement.eye.point.y,
                        camera_placement.eye.point.z))
    cfocus = numpy.array((camera_placement.focus.point.x,
                          camera_placement.focus.point.y,
                          camera_placement.focus.point.z))
    instance.focus = cfocus
    viewdir = ceye - cfocus
    instance.distance = numpy.linalg.norm(viewdir)

    instance.z_up[0] = camera_placement.up.vector.x
    instance.z_up[1] = camera_placement.up.vector.y
    instance.z_up[2] = camera_placement.up.vector.z

    instance.pitch = math.asin(viewdir[2]/instance.distance)
    instance.yaw   = math.atan2(viewdir[1], viewdir[0])

    return instance

  def viewPoint(self):
    p = numpy.array((self.distance * math.cos(self.yaw) * math.cos(self.pitch) + self.focus[0],
                     self.distance * math.sin(self.yaw) * math.cos(self.pitch) + self.focus[1],
                     self.distance *                      math.sin(self.pitch) + self.focus[2]))
    return p
  def cameraOrientation(self):
    OE = self.viewPoint()
    f = self.focus - OE # z
    f = f / tf.transformations.vector_norm(f)
    u = numpy.array((0, 0, 1))            #not aligned y
    r = numpy.cross(u, f) # x
    r = r / tf.transformations.vector_norm(r)
    uy = numpy.cross(f, r)
    uy = uy / tf.transformations.vector_norm(uy)
    m = tf.transformations.identity_matrix()[:3, :3]   #rotation matrix
    m[0, 0] = r[0]
    m[1, 0] = r[1]
    m[2, 0] = r[2]
    m[0, 1] = uy[0]
    m[1, 1] = uy[1]
    m[2, 1] = uy[2]
    m[0, 2] = f[0]
    m[1, 2] = f[1]
    m[2, 2] = f[2]
    return m
  def cameraPlacement(self):
    #TIME = 0.05
    #TIME = 1.0 / 40 * 2.0
    TIME = 1.0 / 30
    view_point = self.viewPoint()
    placement = CameraPlacement()
    placement.interpolation_mode = CameraPlacement.LINEAR
    #placement.interpolation_mode = CameraPlacement.SPHERICAL
    placement.time_from_start = rospy.Duration(TIME)
    # placement.eye.header.stamp = rospy.Time(0.0)
    placement.eye.header.stamp = rospy.Time.now()
    placement.eye.point.x = view_point[0]
    placement.eye.point.y = view_point[1]
    placement.eye.point.z = view_point[2]
    placement.focus.header.stamp = rospy.Time.now()
    placement.focus.point.x = self.focus[0]
    placement.focus.point.y = self.focus[1]
    placement.focus.point.z = self.focus[2]
    placement.up.header.stamp = rospy.Time.now()
    placement.up.vector.x = self.z_up[0]
    placement.up.vector.y = self.z_up[1]
    placement.up.vector.z = self.z_up[2]
    placement.mouse_interaction_mode = CameraPlacement.ORBIT
    return placement
