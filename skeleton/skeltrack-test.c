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

static void on_track_joints (GObject *obj, GAsyncResult *res, gpoing user_data) {

}

int main() {

    return 0;
}