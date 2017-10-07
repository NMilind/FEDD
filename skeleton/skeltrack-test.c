#include "../skeltrack/skeltrack.h"
#include <math.h>
#include <string.h>

static SkeltrackSkeleton *skeleton = NULL;

typedef struct
{
    guint16 *reduced_buffer;
    gint width;
    gint height;
    gint reduced_width;
    gint reduced_height;
} BufferInfo;

static void on_track_joints (GObject *obj, GAsyncResult *res, gpointer user_data) {

    guint i;
    BufferInfo *buffer_info;
    guint16 *reduced;
    gint width, height, reduced_width, reduced_height;
    ClutterContent *content;
    GError *error = NULL;

    buffer_info = (BufferInfo *) user_data;
    reduced = (guint16 *) buffer_info->reduced_buffer;
    width = buffer_info->width;
    height = buffer_info->height;
    reduced_width = buffer_info->reduced_width;
    reduced_height = buffer_info->reduced_height;

    list = skeltrack_skeleton_track_joints_finish (skeleton, res, &error);
}

int main() {

    return 0;
}