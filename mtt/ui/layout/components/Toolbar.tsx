export function Toolbar(props: any): JSX.Element {
  return (
    <div>
      <img src={props.src} />
      {props.children}
    </div>
  );
}
