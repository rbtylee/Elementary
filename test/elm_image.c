#include <Elementary.h>

EAPI_MAIN int
elm_main(int argc, char **argv)
{
   Evas_Object *win = NULL, *image = NULL, *btn = NULL, *bx = NULL;
   char buf[PATH_MAX];
   elm_policy_set(ELM_POLICY_QUIT, ELM_POLICY_QUIT_LAST_WINDOW_CLOSED);
   win = elm_win_util_standard_add("test", "Hello Elementary");
   elm_win_autodel_set(win, EINA_TRUE);
   
   bx = elm_box_add(win);
   evas_object_size_hint_weight_set(bx, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   elm_win_resize_object_add(win, bx);
   evas_object_show(bx);
   
   snprintf(buf, sizeof(buf), "bodhilogo-simple.png");

   image = elm_image_add(win);
    /*if (!elm_image_file_set(image, buf, NULL))
     {
        printf("error: could not load image \"%s\"\n", buf);
        return -1;
     } */
   elm_image_file_set(image, NULL, NULL);
   evas_object_size_hint_weight_set(image, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
   elm_win_resize_object_add(win, image);
   evas_object_show(image);
   
   evas_object_resize(win, 300, 200);
   evas_object_show(win);

   elm_run(); 
   return EXIT_SUCCESS;
}
ELM_MAIN()

//Compile with:
//gcc -o elm_image elm_image.c -g `pkg-config --cflags --libs elementary`
