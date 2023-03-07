// Generated by gencpp from file gripper/TargetDelta.msg
// DO NOT EDIT!


#ifndef GRIPPER_MESSAGE_TARGETDELTA_H
#define GRIPPER_MESSAGE_TARGETDELTA_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace gripper
{
template <class ContainerAllocator>
struct TargetDelta_
{
  typedef TargetDelta_<ContainerAllocator> Type;

  TargetDelta_()
    : target_delta(0.0)  {
    }
  TargetDelta_(const ContainerAllocator& _alloc)
    : target_delta(0.0)  {
  (void)_alloc;
    }



   typedef float _target_delta_type;
  _target_delta_type target_delta;





  typedef boost::shared_ptr< ::gripper::TargetDelta_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::gripper::TargetDelta_<ContainerAllocator> const> ConstPtr;

}; // struct TargetDelta_

typedef ::gripper::TargetDelta_<std::allocator<void> > TargetDelta;

typedef boost::shared_ptr< ::gripper::TargetDelta > TargetDeltaPtr;
typedef boost::shared_ptr< ::gripper::TargetDelta const> TargetDeltaConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::gripper::TargetDelta_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::gripper::TargetDelta_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::gripper::TargetDelta_<ContainerAllocator1> & lhs, const ::gripper::TargetDelta_<ContainerAllocator2> & rhs)
{
  return lhs.target_delta == rhs.target_delta;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::gripper::TargetDelta_<ContainerAllocator1> & lhs, const ::gripper::TargetDelta_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace gripper

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::gripper::TargetDelta_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gripper::TargetDelta_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::gripper::TargetDelta_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::gripper::TargetDelta_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gripper::TargetDelta_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gripper::TargetDelta_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::gripper::TargetDelta_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7f44729b36d41b3490ff1e46feb4d3a0";
  }

  static const char* value(const ::gripper::TargetDelta_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7f44729b36d41b34ULL;
  static const uint64_t static_value2 = 0x90ff1e46feb4d3a0ULL;
};

template<class ContainerAllocator>
struct DataType< ::gripper::TargetDelta_<ContainerAllocator> >
{
  static const char* value()
  {
    return "gripper/TargetDelta";
  }

  static const char* value(const ::gripper::TargetDelta_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::gripper::TargetDelta_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 target_delta\n"
;
  }

  static const char* value(const ::gripper::TargetDelta_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::gripper::TargetDelta_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.target_delta);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TargetDelta_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::gripper::TargetDelta_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::gripper::TargetDelta_<ContainerAllocator>& v)
  {
    s << indent << "target_delta: ";
    Printer<float>::stream(s, indent + "  ", v.target_delta);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GRIPPER_MESSAGE_TARGETDELTA_H