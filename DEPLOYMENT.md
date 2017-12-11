# Deployment

## Describe how you would deploy your web service

As flask application there are a few options for deployment:

- On personal servers, I would install it as a wsgi application in Apache
  using `mod_wsgi`. This just requires creating a script that imports the
  application and configuring Apache to execute the script as a given
  `WSGIScriptAlias`. For a self contained application, the code would be
  installed into a virtual environment.
- To deploy in the _Cloud_, I would build a Docker image which could be
  uploaded directly to services such as AWS or Heroku. The example 
  Dockerfile simply executes the flask application, however the application
  could also be run using a more performant service like gunicorn or mod_wsgi
  within the container. Many cloud services provide on demand scaling and
  load balancing.

## How would you ensure your solution can scale to meet increased demand?

The simplest solution is to leverage whatever infrastructure is already
available. It is much easier to make small modifications to fit in with
efficient working solutions than build an entire new infrastructure. Some
other options can also be considered:

- Deploying on existing cloud services allows for dynamic scaling with very
  little setup. For example, Amazon's AWS has options for dynamic scaling up
  to thousands of instances and will reduce to nothing when demand is low.
  If usage is expected to spike, and generally be uneven, this is a good
  option as there is no waste of resources between spikes.
- Deploying on local hardware can be more effective is load is continuously
  high. A well tuned apache configuration could probably saturate a single
  machine. Beyond that, a setup of a cluster of machines with instances
  running behind a HAProxy load balancer could be used. The instances could be
  managed with a configuration tool like ansible that will designate roles for
  the hardware and change the resources on-the-fly.
- If high demand is expected then the solution would need to profiled
  extensively to identify bottlenecks, and where performance can be improved.
  If the application needs to scale to include more functionality, then the
  current implementation based on ORM software is flexible and can be easily
  expanded. However, if scaling is required for a single functionality then the
  best options would probably be to drop the ORM and use more direct database
  interaction, either with a lower level connector, or constructing SQL
  queries manually. Implementations in other programming languages may also
  provide a speed boost.
- Local caching of results is a must for reducing latency. An in-memory store
  of only the necessary information (e.g. a redis database) would minimise
  slow requests to the remote database. Even simple memoisation for the
  function calls would ensure the most common cases make very few remote
  hits. Solutions will need to consider how quickly the data will become
  stale.
