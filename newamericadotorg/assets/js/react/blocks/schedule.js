import { Component } from 'react';
import { PlusX, Arrow } from '../components/Icons';
import { connect } from 'react-redux';
import { format as formatDate } from 'date-fns';

const NAME = 'scheduleBlock';
const ID = 'schedule-block';

class Session extends Component {
  formatTime = (t) => {
    let time = t.split(':');
    let d = new Date(2000,1,1, ...time);
    return formatDate(d, 'hh:mma');
  };
  render() {
    let { name, description, start_time, end_time, speakers, expanded, expand, hasDesc } = this.props;
    return (
      <div className={`schedule-block__sessions__session ${expanded && hasDesc ? 'expanded' : ''}`}>
        <div className="schedule-block__sessions__session__heading">
          <div className="schedule-block__sessions__session__heading__title" onClick={expand}>
            <label className="block button--text">
              {this.formatTime(start_time)}{end_time && ' - '}{this.formatTime(end_time)}
            </label>
            <h3 className="margin-15">{name}</h3>
            {hasDesc &&
              <PlusX x={expanded} />
            }
          </div>
        </div>
        <span className="schedule-block__sessions__session__description">
          {description && <div className="post-body margin-bottom-35" dangerouslySetInnerHTML={{__html: description}} />}
        {speakers.length>0 &&
          <span>
            <label className="block button--text margin-bottom-35">Speakers</label>
            <div className="schedule-block__sessions__session__speakers">
              {speakers.map((s,i)=>(
                <div className="schedule-block__sessions__session__speakers__speaker margin-bottom-25">
                  <label className="bold block">{s.name}
                  {s.twitter &&
                    <a href={s.twitter} target="_blank">
                      <i className="fa fa-twitter"></i>
                    </a>}
                  </label>
                  {s.title && <label className="caption block">{s.title}</label>}
                </div>
              ))}
            </div>
          </span>
        }
        </span>
      </div>
    );
  }
}


class APP extends Component {
  state = { }
  expand = (scheduleIndex) => {
    if(this.state[scheduleIndex]) this.setState({ [scheduleIndex]: false });
    else this.setState({ [scheduleIndex]: true });
  }
  render(){
    let { days } = this.props;
    if(!days) return null;
    days = JSON.parse(days);
    return (
      <div className={`schedule-block`}>
        {days.map((sessions,i)=>(
          <div className="schedule-block__day">
            <div className="schedule-block__sessions">
              {sessions.map((s,i)=>(
                <Session hasDesc={s.description || s.speakers.length > 0} expanded={this.state[i]} expand={()=>{this.expand(i)}} {...s} />
              ))}
            </div>
          </div>
        ))}
      </div>
    );
  }
}



export default { APP, NAME, ID, MULTI: true };
