//  Copyright Ryan Faulkner 2013.
//  see LICENSE

#include <boost/python/module.hpp>
#include <boost/python/def.hpp>

char const* noop()
{
   return "noop";
}

BOOST_PYTHON_MODULE(cjoin_ext)
{
    using namespace boost::python;
    def("noop", noop);
}
