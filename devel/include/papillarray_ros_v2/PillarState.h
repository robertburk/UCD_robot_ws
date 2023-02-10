// Generated by gencpp from file papillarray_ros_v2/PillarState.msg
// DO NOT EDIT!


#ifndef PAPILLARRAY_ROS_V2_MESSAGE_PILLARSTATE_H
#define PAPILLARRAY_ROS_V2_MESSAGE_PILLARSTATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace papillarray_ros_v2
{
template <class ContainerAllocator>
struct PillarState_
{
  typedef PillarState_<ContainerAllocator> Type;

  PillarState_()
    : header()
    , id(0)
    , dX(0.0)
    , dY(0.0)
    , dZ(0.0)
    , fX(0.0)
    , fY(0.0)
    , fZ(0.0)
    , in_contact(false)
    , slip_state(0)  {
    }
  PillarState_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , id(0)
    , dX(0.0)
    , dY(0.0)
    , dZ(0.0)
    , fX(0.0)
    , fY(0.0)
    , fZ(0.0)
    , in_contact(false)
    , slip_state(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int32_t _id_type;
  _id_type id;

   typedef float _dX_type;
  _dX_type dX;

   typedef float _dY_type;
  _dY_type dY;

   typedef float _dZ_type;
  _dZ_type dZ;

   typedef float _fX_type;
  _fX_type fX;

   typedef float _fY_type;
  _fY_type fY;

   typedef float _fZ_type;
  _fZ_type fZ;

   typedef uint8_t _in_contact_type;
  _in_contact_type in_contact;

   typedef int32_t _slip_state_type;
  _slip_state_type slip_state;





  typedef boost::shared_ptr< ::papillarray_ros_v2::PillarState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::papillarray_ros_v2::PillarState_<ContainerAllocator> const> ConstPtr;

}; // struct PillarState_

typedef ::papillarray_ros_v2::PillarState_<std::allocator<void> > PillarState;

typedef boost::shared_ptr< ::papillarray_ros_v2::PillarState > PillarStatePtr;
typedef boost::shared_ptr< ::papillarray_ros_v2::PillarState const> PillarStateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::papillarray_ros_v2::PillarState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::papillarray_ros_v2::PillarState_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::papillarray_ros_v2::PillarState_<ContainerAllocator1> & lhs, const ::papillarray_ros_v2::PillarState_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.id == rhs.id &&
    lhs.dX == rhs.dX &&
    lhs.dY == rhs.dY &&
    lhs.dZ == rhs.dZ &&
    lhs.fX == rhs.fX &&
    lhs.fY == rhs.fY &&
    lhs.fZ == rhs.fZ &&
    lhs.in_contact == rhs.in_contact &&
    lhs.slip_state == rhs.slip_state;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::papillarray_ros_v2::PillarState_<ContainerAllocator1> & lhs, const ::papillarray_ros_v2::PillarState_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace papillarray_ros_v2

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::papillarray_ros_v2::PillarState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::papillarray_ros_v2::PillarState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::papillarray_ros_v2::PillarState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::papillarray_ros_v2::PillarState_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::papillarray_ros_v2::PillarState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::papillarray_ros_v2::PillarState_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::papillarray_ros_v2::PillarState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f75cd8df721a8e7158c9671c32de7f98";
  }

  static const char* value(const ::papillarray_ros_v2::PillarState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf75cd8df721a8e71ULL;
  static const uint64_t static_value2 = 0x58c9671c32de7f98ULL;
};

template<class ContainerAllocator>
struct DataType< ::papillarray_ros_v2::PillarState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "papillarray_ros_v2/PillarState";
  }

  static const char* value(const ::papillarray_ros_v2::PillarState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::papillarray_ros_v2::PillarState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"int32 id\n"
"float32 dX\n"
"float32 dY\n"
"float32 dZ\n"
"float32 fX\n"
"float32 fY\n"
"float32 fZ\n"
"bool in_contact\n"
"int32 slip_state\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::papillarray_ros_v2::PillarState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::papillarray_ros_v2::PillarState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.id);
      stream.next(m.dX);
      stream.next(m.dY);
      stream.next(m.dZ);
      stream.next(m.fX);
      stream.next(m.fY);
      stream.next(m.fZ);
      stream.next(m.in_contact);
      stream.next(m.slip_state);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PillarState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::papillarray_ros_v2::PillarState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::papillarray_ros_v2::PillarState_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.id);
    s << indent << "dX: ";
    Printer<float>::stream(s, indent + "  ", v.dX);
    s << indent << "dY: ";
    Printer<float>::stream(s, indent + "  ", v.dY);
    s << indent << "dZ: ";
    Printer<float>::stream(s, indent + "  ", v.dZ);
    s << indent << "fX: ";
    Printer<float>::stream(s, indent + "  ", v.fX);
    s << indent << "fY: ";
    Printer<float>::stream(s, indent + "  ", v.fY);
    s << indent << "fZ: ";
    Printer<float>::stream(s, indent + "  ", v.fZ);
    s << indent << "in_contact: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.in_contact);
    s << indent << "slip_state: ";
    Printer<int32_t>::stream(s, indent + "  ", v.slip_state);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PAPILLARRAY_ROS_V2_MESSAGE_PILLARSTATE_H
