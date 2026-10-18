#include <udf.h>

DEFINE_PROFILE(my_changing_velocity, thread, i)
{
face_t f;
double t = CURRENT_TIME;
double velocity;
double AIN = 2.592834075373901;
double AOUT = 1.2964170376869506;
double OMEGAIN = 2.0734511513692633;
double OMEGAOUT = 1.0367255756846316;

 /*inhalation no 1*/
if (t<1.5151515151515151)
{
velocity = AIN*sin(OMEGAIN*t);
}
/*exhalation no 1*/
else if(t>=1.5151515151515151 && t<4.545454545454546)
{
velocity = -AOUT*sin(OMEGAOUT*(t-1.5151515151515151));
}
else
{
velocity = 0;
}
begin_f_loop(f, thread)
{
F_PROFILE(f, thread, i) = velocity;
}
end_f_loop(f, thread)
}