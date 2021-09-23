# cvmfs-manage-replicas

For documentation on manage-replicas see the comments in
[manage-replicas.conf](https://github.com/cvmfs-contrib/cvmfs-manage-replicas/blob/master/manage-replicas.conf).

rpm distributions of this package for CentOS/RHEL are available in
[cvmfs-contrib](https://cvmfs-contrib.githup.io).

To invoke from cron, use the additional script manage-replicas-log which
allows $MAXPARALLELMANAGE replicas to happen in parallel and combines
their output in `/var/log/cvmfs/manage-replicas.log`.

## Example -- rebuilding a stratum 1

One simple way to use this package is as a way to rebuild a cvmfs
stratum 1 from scratch, taking fresh snapshots of all the repositories
off an old one called `stratum.one.fqdn`.
Assuming you have an `add-repository` script as used by default for the
addcmd (you could use the package's default by putting
`/usr/share/cvmfs-manage-replicas` in the PATH), then
`/etc/cvmfs/manage-replicas.conf` would look like this:
```
remcmd true
keysource cvmfs-contrib/config-repo/master/etc/cvmfs/keys
replist http://stratum.one.fqdn:8000/cvmfs/info/v1/repositories.json
source http://stratum.one.fqdn:8000
repos *
```
Then run `manage-replicas-log` 4 times with nohup in the background, and
possibly also from cron in case some of the snaphots fail and it needs
to be run again.
You may want to set MAXPARALLELMANAGE a little higher, perhaps to 8 in
order to get it to rebuild faster, depending on how heavily loaded your
machines are.
On a big stratum 1 it will likely take several days or even a week,
depending on the speed of the disk hardware and network. 

If your `add-repository` script accepts `continue` as an option in place
of the stratum one URL (as the provided script does), then add the
`manage-replicas -c` option to enable restarting a big initial snapshot
if it fails for some reason.
This option implies `remcmd true` because otherwise a failure to add a
repository causes it to be immediately removed.

The `keysource` option will result in automatically downloading missing
repository keys from github.

The output while each process is running goes to
`/var/run/cvmfs/manage-replicas.log.*`, and when each process finishes
it appends its output to `/var/log/cvmfs/manage-replicas.log`.
It will likely need to be nursed along, especially if source files have
disappeared or gotten corrupted on the stratum 1 being copied.
With the huge numbers of files involved, that is pretty typical.
The files can be re-downloaded from some other stratum1 by hand.

You'll need to edit /etc/cvmfs/repositories.d/*/server.conf after
completion to copy the CVMFS_STRATUM0 setting on each repository from
your original machine.
Alternatively, if you manage all your repositories via
manage-replicas.conf, then when you copy manage-replicas.conf from your
original machine the CVMFS_STRATUM0 settings will be automatically
updated the next time manage-replicas runs.
