// Generated by gencpp from file papillarray_ros_v2/StopSlipDetectionRequest.msg
// DO NOT EDIT!


#ifndef PAPILLARRAY_ROS_V2_MESSAGE_STOPSLIPDETECTIONREQUEST_H
#define PAPILLARRAY_ROS_V2_MESSAGE_STOPSLIPDETECTIONREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace papillarray_ros_v2
{
template <class ContainerAllocator>
struct StopSlipDetectionRequest_
{
  typedef StopSlipDetectionRequest_<ContainerAllocator> Type;

  StopSlipDetectionRequest_()
    {
    }
  StopSlipDetectionRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> const> ConstPtr;

}; // struct StopSlipDetectionRequest_

typedef ::papillarray_ros_v2::StopSlipDetectionRequest_<std::allocator<void> > StopSlipDetectionRequest;

typedef boost::shared_ptr< ::papillarray_ros_v2::StopSlipDetectionRequest > StopSlipDetectionRequestPtr;
typedef boost::shared_ptr< ::papillarray_ros_v2::StopSlipDetectionRequest const> StopSlipDetectionRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace papillarray_ros_v2

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "papillarray_ros_v2/StopSlipDetectionRequest";
  }

  static const char* value(const ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct StopSlipDetectionRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::papillarray_ros_v2::StopSlipDetectionRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // PAPILLARRAY_ROS_V2_MESSAGE_STOPSLIPDETECTIONREQUEST_H