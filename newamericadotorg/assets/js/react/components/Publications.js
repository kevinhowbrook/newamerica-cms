import { Component } from 'react';
import { format as formatDate } from 'date-fns';
import { connect } from 'react-redux';
import ScrollArea from 'react-scrollbar';
import { RadioButton } from './Inputs';


export class Filter extends Component {
  constructor(props){
    super(props);
    this.state = {
      expanded: props.expanded || false
    }
  }

  handleChange = (event) => {}

  toggle = () => {
    this.setState({ expanded: !this.state.expanded });
  }

  label = () => {
    return (
      <label className="program__publications-filters__filter__heading block bold margin-25" onClick={this.toggle}>
        {this.props.label}
        <div className="icon">
          {this.state.expanded && <i className="fa fa-minus" />}
          {!this.state.expanded && <i className="fa fa-plus" />}
        </div>
      </label>
    );
  }
}

export class TypeFilter extends Filter {
  handleChange = (event) => {
    let { setQuery, history, location, program } = this.props;
    let params = new URLSearchParams(location.search.replace('?', ''));
    setQuery({
      content_type: event.target.value,
      page: 1
    }, true);
    history.push(`${program ? program.url : '/'}${event.target.getAttribute('data-slug')}/?${params.toString()}`);
  }

  render(){
    let { types, setQueryParam, location : { pathname }, response: { params: { query } } } = this.props;
    return (
      <div className={`program__publications-filters__filter type-filter ${this.state.expanded ? 'expanded' : ''}`}>
        {this.label()}
        <form>
          <RadioButton label={'All'} value={''} data-slug="publications" checked={query.content_type=='' || pathname.indexOf('publications') != -1} onChange={this.handleChange} />
          {types.map((t,i)=>(
            <RadioButton label={t.title} value={t.api_name} data-slug={t.slug} checked={query.content_type==t.api_name || pathname.indexOf(`/${t.slug}/`) != -1} onChange={this.handleChange}/>
          ))}
        </form>
      </div>
    );
  }
}

export class ProgramFilter extends Filter {
  handleChange = (event) => {
    let { setQuery, history, location } = this.props;
    let params = new URLSearchParams(location.search.replace('?', ''));
    if(event.target.value == '') {
      params.delete('programId');
    } else {
      params.set('programId', event.target.value);
    }

    history.push(`${location.pathname}?${params.toString()}`);
    setQuery({
      program_id: event.target.value,
      page: 1,
    }, true);
  }

  render(){
    let { programs, response: { params: { query } } } = this.props;

    return (
      <div className={`program__publications-filters__filter program-filter ${this.state.expanded ? 'expanded' : ''}`}>
        {this.label()}
        <form>
          <RadioButton label={'All'} value={''} checked={query.program_id==''} onChange={this.handleChange} />
          {programs.map((p,i)=>(
            <RadioButton label={p.title} value={p.id} checked={+query.program_id===p.id} onChange={this.handleChange}/>
          ))}
        </form>
      </div>
    );
  }
}

export class SubprogramFilter extends Filter {
  handleChange = (event) => {
    let { setQuery, history, location, program } = this.props;
    let params = new URLSearchParams(location.search.replace('?', ''));

    if(event.target.value == '') {
      params.delete('projectId');
    } else {
      params.set('projectId', event.target.value);
    }

    history.push(`${location.pathname}?${params.toString()}`);
    setQuery({
      subprogram_id: event.target.value,
      page: 1,
    }, true);

  }

  render(){
    let { subprograms, response: { params: { query } } } = this.props;
    return (
      <div className={`program__publications-filters__filter subprogram-filter ${this.state.expanded ? 'expanded' : ''}`}>
        {this.label()}
        <form>
          <RadioButton label={'All'} value={''} checked={query.subprogram_id==''} onChange={this.handleChange} />
          {subprograms.map((p,i)=>(
            <RadioButton label={p.name} value={p.id} checked={+query.subprogram_id===p.id} onChange={this.handleChange}/>
          ))}
        </form>
      </div>
    );
  }
}

export class DateFilter extends Filter {
  handleChange = (event) => {}

  render(){
    return (
      <div className={`program__publications-filters__filter date-filter ${this.state.expanded ? 'expanded' : ''}`}>
        {this.label()}
        <form>
        </form>
      </div>
    );
  }
}

export class TopicFilter extends Filter {
  handleChange = (event) => {}

  render(){
    return (
      <div className={`program__publications-filters__filter topic-filter ${this.state.expanded ? 'expanded' : ''}`}>
        {this.label()}
        <form>
        </form>
      </div>
    );
  }
}

export const PublicationListItem = ({ post }) => (
  <div className="card list">
    <a href={post.url}>
      <div className={`card__image ${!post.story_image ? 'no-image' : ''}`}>
        <div className="card__image__img" style={{ backgroundImage: `url(${post.story_image})` }}></div>
      </div>
      </a>
    <div className="card__text">
      <a href={post.url}>
        <label className="card__text__date margin-top-0 block">{formatDate(post.date, 'MMM. Do, YYYY')}</label>
        <label className="card__text__title bold block">{post.title}</label>
      </a>
      {post.authors &&
      <label className="card__text__description subtitle block">
        {post.authors.map((a, i)=>(
          <span>
            <a href={a.url} className="inline">{a.first_name} {a.last_name}</a>
            {i != (post.authors.length-1) &&
              <span> + </span>
            }
          </span>
        ))}
      </label>}
      <a href={post.url}>
        <label className="card__text__program caption margin-bottom-0 block">
          {post.programs[0] ? post.programs[0].name : ''} {post.content_type ? post.content_type.title : ''}
        </label>
      </a>
    </div>
  </div>
);

export const LoadingDots = ({ color='black' }) => (
  <label className={`button--text loading-dots centered ${color} block`}>
    <span>.</span><span>.</span><span>.</span>
  </label>
);

export class PublicationsList extends Component {
  loadMore = () => {
    let { fetchAndAppend, setQueryParam, response } = this.props;
    if(!response.hasNext || response.isFetching) return;
    this.isLoadingMore = true;
    setQueryParam('page', response.page+1);
    fetchAndAppend(this.triggerScrollEvents);
  }

  triggerScrollEvents = () => {
    setTimeout(()=>{
      this.isLoadingMore = false;
      this.props.dispatch({
        type: 'TRIGGER_SCROLL_EVENTS',
        component: 'site'
      });
    });
  }

  render(){
    let { response, fetchAndAppend } = this.props;
    let { results, isFetching, hasNext } = response;
    if(results.length===0 && !isFetching){
      return (
        <label className="bold block centered">No results found</label>
      );
    }

    if(isFetching && !this.isLoadingMore){
      return (
        <div className="program__publications-list-wrapper">
          <div className="program__publications-list margin-top-60">
              <LoadingDots />
          </div>
        </div>
      );
    }

    return (
      <div className="program__publications-list-wrapper">
        <div className="program__publications-list">
            {results.map((post, i ) => (
              <PublicationListItem post={post} />
            ))}
        </div>
        {hasNext &&
        <div className="program__publications-list-load-more margin-top-10">
          <label className={`button ${isFetching ? 'is-fetching' : ''}`} onClick={this.loadMore}>
            <span className="load-more-label">Load More</span>
            {isFetching && <span className="loading-dots--absolute">
              <span>.</span><span>.</span><span>.</span>
            </span>}
          </label>
        </div>}
      </div>
    );
  }
}

class _FilterGroup extends Component {
  state = { lastScrollPosition: 0, isLoadingMore: true }

  componentDidMount(){
    this.reloadScrollEvents();
  }

  componentDidUpdate(prevProps){
    let { location, program, setQuery, response } = this.props;

    if(location !== prevProps.location){
      this.reloadScrollEvents();
      let slug = location.pathname.match(/.+\/(.+)\/$/i)[1];
      let type = program.content_types.find((t)=>(t.slug === slug));
      // click on publications link in nav:
      if(slug=='publications' && location.search==''){
        setQuery({
          content_type: '',
          subprogram_id: '',
          page: 1
        }, true);
      }

      if(window.scrollY > 300){
        window.scrollTo(0, 300);
      }
      // if(+document.body.style.top.replace('px', '') < -365){
      //   this.state.lastScrollPosition = 365;
      //   this.enableScroll();
      //   this.disableScroll(false);
      // }

    }
  }

  disableScroll = (update) => {
    // if(update !== false) this.state.lastScrollPosition = this.props.windowScrollPosition;
    // document.body.classList.add('scroll-disabled');
    // document.body.style.top = -this.state.lastScrollPosition + 'px';
  }

  enableScroll = () => {
    // document.body.classList.remove('scroll-disabled');
    // document.body.style.top = '';
    // window.scrollTo(0, this.state.lastScrollPosition);
  }

  reloadScrollEvents(){
    this.props.dispatch({
      type: 'RELOAD_SCROLL_EVENTS',
      component: 'site'
    });
  }

  render(){
    return (
      <div className={`program__publications-filters scroll-target`}
        data-scroll-top-offset="-15"
        onMouseEnter={this.disableScroll}
        onTouchStart={this.disableScroll}
        onMouseLeave={this.enableScroll}
        onTouchEnd={this.enableScroll}>
        <div className={`program__publications-filters__sticky-wrapper`}>
          <ScrollArea className="program__publications-filters__scroll-area">
            {this.props.children}
          </ScrollArea>
        </div>
      </div>
    )
  }
}

const mapStateToProps = (state) => ({
  windowScrollPosition: state.site.scroll.position
});

export const FilterGroup = connect(mapStateToProps)(_FilterGroup);
